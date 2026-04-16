from fastapi import APIRouter

from app.schemas.node import NodeEnergyData
from app.services.node_service import node_data_service

router = APIRouter()


@router.get("/health")
def health_check() -> dict:
    return {
        "status": "ok",
        "service": "poe-backend"
    }


@router.post("/nodes/data")
def ingest_node_data(payload: NodeEnergyData) -> dict:
    saved_item = node_data_service.save_node_data(payload)

    return {
        "message": "Node data received and stored successfully",
        "data": saved_item
    }


@router.get("/nodes/data")
def list_node_data() -> dict:
    items = node_data_service.get_all_node_data()

    return {
        "count": len(items),
        "items": items
    }