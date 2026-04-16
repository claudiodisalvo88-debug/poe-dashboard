from datetime import datetime
from pydantic import BaseModel, Field


class NodeEnergyData(BaseModel):
    timestamp: datetime
    node_id: str = Field(..., min_length=1, max_length=100)
    watt: float = Field(..., gt=0)
    energy_wh: float = Field(..., ge=0)
    volt: float | None = Field(default=None, gt=0)
    ampere: float | None = Field(default=None, ge=0)
    state: str | None = Field(default=None, max_length=50)
