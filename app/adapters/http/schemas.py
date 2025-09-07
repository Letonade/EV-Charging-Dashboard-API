from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional

class PageMeta(BaseModel):
    total: int
    limit: int
    offset: int

class Page(BaseModel):
    data: list
    meta: PageMeta

class ErrorResponse(BaseModel):
    error: str
    detail: Optional[str] = None

class StationOut(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    name: str
    latitude: float
    longitude: float
    status: str
    connectors: List[str] = Field(default_factory=list)

class StationStatusUpdateIn(BaseModel):
    status: str

class SessionOut(BaseModel):
    id: str
    vehicle_id: str
    station_id: str
    started_at: str # ISO 8601
    ended_at: Optional[str] = None
    energy_kwh: float
    cost_eur: float