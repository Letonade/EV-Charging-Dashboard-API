from typing import List, Optional
from datetime import datetime, timedelta
from ...core.entities import ChargingSession
from ...application.ports.session_repository import SessionRepository


class InMemorySessionRepository(SessionRepository):
    def __init__(self):
        now = datetime.utcnow()
        self._sessions = [
            ChargingSession(
                id="CS-1001",
                vehicle_id="V-TRUCK-01",
                station_id="S-001",
                started_at=now - timedelta(hours=6),
                ended_at=now - timedelta(hours=5, minutes=15),
                energy_kwh=120.5,
                cost_eur=48.20
            ),
            ChargingSession(
                id="CS-1002",
                vehicle_id="V-CAR-77",
                station_id="S-002",
                started_at=now - timedelta(hours=2, minutes=30),
                ended_at=None,  # encore en cours
                energy_kwh=34.2,
                cost_eur=0.0
            ),
            ChargingSession(
                id="CS-1003",
                vehicle_id="V-TRUCK-15",
                station_id="S-003",
                started_at=now - timedelta(days=1, hours=3),
                ended_at=now - timedelta(days=1, hours=2, minutes=40),
                energy_kwh=200.0,
                cost_eur=80.0
            ),
            ChargingSession(
                id="CS-1004",
                vehicle_id="V-CAR-21",
                station_id="S-004",
                started_at=now - timedelta(hours=10),
                ended_at=now - timedelta(hours=9, minutes=45),
                energy_kwh=18.7,
                cost_eur=7.50
            ),
            ChargingSession(
                id="CS-1005",
                vehicle_id="V-TRUCK-88",
                station_id="S-005",
                started_at=now - timedelta(minutes=90),
                ended_at=now - timedelta(minutes=20),
                energy_kwh=95.3,
                cost_eur=39.60
            ),
            ChargingSession(
                id="CS-1006",
                vehicle_id="V-CAR-44",
                station_id="S-006",
                started_at=now - timedelta(hours=4, minutes=10),
                ended_at=now - timedelta(hours=3, minutes=5),
                energy_kwh=45.0,
                cost_eur=18.75
            ),
        ]

    def list_sessions(self, *, limit: int = 50, since: Optional[datetime] = None) -> List[ChargingSession]:
        items = self._sessions
        if since:
            items = [s for s in items if s.started_at >= since]
        return items[:limit]
