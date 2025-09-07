from typing import List, Optional
from ...core.entities import Station, Location
from ...core.enums import StationStatus
from ...application.ports.station_repository import StationRepository


class InMemoryStationRepository(StationRepository):
    def __init__(self):
        # seed demo data
        self._stations = {
            "S-001": Station(
                id="S-001",
                name="Depot A - Paris",
                location=Location(latitude=48.8566, longitude=2.3522),
                status=StationStatus.AVAILABLE,
                connectors=["CCS2", "CHAdeMO"]
            ),
            "S-002": Station(
                id="S-002",
                name="Highway Hub 12 - Lyon",
                location=Location(latitude=45.7640, longitude=4.8357),
                status=StationStatus.OCCUPIED,
                connectors=["CCS2"]
            ),
            "S-003": Station(
                id="S-003",
                name="Regional Station - Marseille Port",
                location=Location(latitude=43.2965, longitude=5.3698),
                status=StationStatus.OUT_OF_SERVICE,
                connectors=["CCS2", "Type2"]
            ),
            "S-004": Station(
                id="S-004",
                name="Depot B - Lille Logistics",
                location=Location(latitude=50.6292, longitude=3.0573),
                status=StationStatus.AVAILABLE,
                connectors=["CCS2"]
            ),
            "S-005": Station(
                id="S-005",
                name="Highway Hub 21 - Bordeaux",
                location=Location(latitude=44.8378, longitude=-0.5792),
                status=StationStatus.OCCUPIED,
                connectors=["CHAdeMO", "Type2"]
            ),
            "S-006": Station(
                id="S-006",
                name="Urban Fast Charge - Toulouse",
                location=Location(latitude=43.6047, longitude=1.4442),
                status=StationStatus.AVAILABLE,
                connectors=["CCS2", "CHAdeMO", "Type2"]
            ),
        }

    def list_stations(self) -> List[Station]:
        return list(self._stations.values())

    def get_station(self, station_id: str) -> Optional[Station]:
        return self._stations.get(station_id)

    def set_status(self, station_id: str, status: StationStatus) -> Station:
        st = self._stations.get(station_id)
        if not st:
            raise KeyError(f"Station {station_id} not found")
        st.status = status
        self._stations[station_id] = st
        return st
