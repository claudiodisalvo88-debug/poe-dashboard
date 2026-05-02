import os
from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import init_db
from schemas import (
    NodeIngestPayload,
    IngestResponse,
    SummaryResponse,
    ReputationItem,
)
from services import (
    ingest_node_data,
    get_nodes_data,
    get_summary_data,
    get_reputation_data,
)
from internal_generator import start_internal_generator


APP_NAME = os.getenv("POE_APP_NAME", "Proof of Energy API")
APP_VERSION = os.getenv("POE_APP_VERSION", "1.2.0")
POE_CORS_ORIGINS = os.getenv("POE_CORS_ORIGINS", "*")


app = FastAPI(
    title=APP_NAME,
    description="Proof of Energy MVP API: live nodes, history, KPI and Energy Reputation ranking.",
    version=APP_VERSION,
)


cors_origins = [
    origin.strip()
    for origin in POE_CORS_ORIGINS.split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins if cors_origins else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


init_db()


@app.on_event("startup")
def startup_event():
    start_internal_generator()


def _parse_timestamp(value):
    """
    Converte timestamp ISO in datetime sempre timezone-aware UTC.
    Evita errori tra datetime offset-naive e offset-aware.
    """
    if not value:
        return datetime.min.replace(tzinfo=timezone.utc)

    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))

        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)

        return parsed

    except Exception:
        return datetime.min.replace(tzinfo=timezone.utc)


@app.get("/", tags=["System"])
def home():
    return {
        "status": "ok",
        "service": APP_NAME,
        "version": APP_VERSION,
        "endpoints": [
            "/health",
            "/live",
            "/history",
            "/kpi",
            "/ranking",
            "/ingest",
        ],
    }


@app.get("/health", tags=["System"])
def health():
    return {
        "status": "healthy",
        "service": APP_NAME,
        "version": APP_VERSION,
    }


@app.post("/ingest", tags=["Ingest"], response_model=IngestResponse)
def ingest(payload: NodeIngestPayload):
    return ingest_node_data(payload)


# NEW STANDARD ENDPOINTS

@app.get("/live", tags=["Nodes"])
def live():
    """
    Restituisce l'ultimo record valido per ogni nodo.
    """
    data = get_nodes_data()

    if not data:
        return []

    latest_by_node = {}

    for row in data:
        node_id = row.get("node_id")
        timestamp = row.get("timestamp")

        if not node_id or not timestamp:
            continue

        row_time = _parse_timestamp(timestamp)

        if (
            node_id not in latest_by_node
            or row_time > _parse_timestamp(latest_by_node[node_id].get("timestamp"))
        ):
            latest_by_node[node_id] = row

    return list(latest_by_node.values())


@app.get("/history", tags=["Nodes"])
def history(limit: int = 100):
    """
    Restituisce gli ultimi N record ordinati dal più recente al più vecchio.

    Esempio:
    /history?limit=5
    """
    data = get_nodes_data()

    if not data:
        return []

    clean_data = [
        row for row in data
        if row.get("timestamp") and row.get("node_id")
    ]

    sorted_data = sorted(
        clean_data,
        key=lambda row: _parse_timestamp(row.get("timestamp")),
        reverse=True,
    )

    return sorted_data[:limit]


@app.get("/kpi", tags=["Analytics"], response_model=SummaryResponse)
def kpi():
    return get_summary_data()


@app.get("/ranking", tags=["Analytics"], response_model=list[ReputationItem])
def ranking():
    return get_reputation_data()


# OLD COMPATIBILITY ENDPOINTS

@app.get("/nodes", tags=["Compatibility"])
def get_nodes():
    return get_nodes_data()


@app.get("/summary", tags=["Compatibility"], response_model=SummaryResponse)
def summary():
    return get_summary_data()


@app.get("/reputation", tags=["Compatibility"], response_model=list[ReputationItem])
def reputation():
    return get_reputation_data()
