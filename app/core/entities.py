from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime
from .enums import VehicleType, OwnerType, StationStatus


class Location(BaseModel):
    latitude: float
    longitude: float


class Station(BaseModel):
    id: str
    name: str
    location: Location
    status: StationStatus = StationStatus.AVAILABLE
    connectors: List[str] = Field(default_factory=list)  # e.g., ["CCS2", "CHAdeMO"]


class Vehicle(BaseModel):
    id: str
    vehicle_type: VehicleType
    owner_type: OwnerType
    owner_name: Optional[str] = None


class ChargingSession(BaseModel):
    id: str
    vehicle_id: str
    station_id: str
    started_at: datetime
    ended_at: Optional[datetime] = None
    energy_kwh: float = 0.0
    cost_eur: float = 0.0
