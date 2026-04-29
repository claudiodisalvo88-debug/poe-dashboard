import os
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

APP_NAME = os.getenv("POE_APP_NAME", "Proof of Energy API")
APP_VERSION = os.getenv("POE_APP_VERSION", "1.1.0")
POE_CORS_ORIGINS = os.getenv("POE_CORS_ORIGINS", "*")

app = FastAPI(
    title=APP_NAME,
    description="API del MVP Proof of Energy per monitoraggio nodi, summary energetico e ranking di Energy Reputation.",
    version=APP_VERSION,
)

cors_origins = [origin.strip() for origin in POE_CORS_ORIGINS.split(",") if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins if cors_origins else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()


@app.get("/", tags=["System"])
def home():
    return {
        "status": "ok",
        "service": APP_NAME,
        "version": APP_VERSION,
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


@app.get("/nodes", tags=["Nodes"])
def get_nodes():
    return get_nodes_data()


@app.get("/summary", tags=["Analytics"], response_model=SummaryResponse)
def summary():
    return get_summary_data()


@app.get("/reputation", tags=["Analytics"], response_model=list[ReputationItem])
def reputation():
    return get_reputation_data()
