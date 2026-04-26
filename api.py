from fastapi import FastAPI
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

app = FastAPI(
    title="Proof of Energy API",
    description="API del MVP Proof of Energy per monitoraggio nodi, summary energetico e ranking di Energy Reputation.",
    version="1.1.0"
)

init_db()


@app.get("/", tags=["System"])
def home():
    return {
        "status": "ok",
        "service": "Proof of Energy API",
        "version": "1.1.0"
    }


@app.get("/health", tags=["System"])
def health():
    return {
        "status": "healthy"
    }


@app.post("/ingest", tags=["Ingest"], response_model=IngestResponse)
def ingest(payload: NodeIngestPayload):
    return ingest_node_data(payload)


@app.get("/nodes", tags=["Nodes"])
def get_nodes():
    return get_nodes_data()


@app.get("/summary", tags=["Analytics"], response_model=SummaryResponse)
def summary():
    return get_summary_data()


@app.get("/reputation", tags=["Analytics"], response_model=list[ReputationItem])
def reputation():
    return get_reputation_data()