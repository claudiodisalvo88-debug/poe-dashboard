from logger import logger
import os
import math
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import init_db
from schemas import NodeIngestPayload, IngestResponse, SummaryResponse, ReputationItem
from services import (
    ingest_node_data,
    get_nodes_data,
    get_summary_data,
    get_reputation_data
)
from internal_generator import start_internal_generator


app = FastAPI(
    title="Proof of Energy API",
    version="1.2.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

init_db()


@app.on_event("startup")
def startup():
    start_internal_generator()


def clean(row):
    return {
        k: (None if isinstance(v, float) and (math.isnan(v) or math.isinf(v)) else v)
        for k, v in row.items()
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/ingest", response_model=IngestResponse)
def ingest(payload: NodeIngestPayload):
    logger.info(f"INGEST {payload.node_id} | watt={payload.watt} | energy={payload.energy_wh}")
    return ingest_node_data(payload)

@app.get("/live")
def live():
    data = get_nodes_data()
    latest = {}

    for r in data:
        latest[r["node_id"]] = clean(r)

    return list(latest.values())


@app.get("/history")
def history(limit: int = 100):
    data = get_nodes_data()
    return data[-limit:]


@app.get("/kpi", response_model=SummaryResponse)
def kpi():
    return get_summary_data()


@app.get("/ranking", response_model=list[ReputationItem])
def ranking():
    return get_reputation_data()
