from typing import List
from ...core.entities import Station
from ...core.enums import StationStatus
from ..ports.station_repository import StationRepository


class StationService:
    def __init__(self, repo: StationRepository):
        self._repo = repo

    def list(self) -> List[Station]:
        return self._repo.list_stations()

    def set_status(self, station_id: str, status: StationStatus) -> Station:
        return self._repo.set_status(station_id, status)
