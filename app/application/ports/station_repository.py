from typing import List, Optional
from ...core.entities import Station
from ...core.enums import StationStatus


class StationRepository:
    def list_stations(self) -> List[Station]:
        raise NotImplementedError

    def get_station(self, station_id: str) -> Optional[Station]:
        raise NotImplementedError

    def set_status(self, station_id: str, status: StationStatus) -> Station:
        raise NotImplementedError