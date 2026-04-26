from pydantic import BaseModel


class NodeIngestPayload(BaseModel):
    timestamp: str
    node_id: str
    watt: float
    energy_wh: float


class IngestResponse(BaseModel):
    status: str
    message: str
    node_id: str


class SummaryResponse(BaseModel):
    total_energy: float
    avg_power: float
    nodes: int
    records: int


class ReputationItem(BaseModel):
    node_id: str
    reputation: float
    energy: float
    stability: float