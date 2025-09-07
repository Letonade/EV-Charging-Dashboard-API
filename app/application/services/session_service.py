from typing import List, Optional
from datetime import datetime
from ...core.entities import ChargingSession
from ..ports.session_repository import SessionRepository


class SessionService:
    def __init__(self, repo: SessionRepository):
        self._repo = repo


    def list(self, *, limit: int = 50, since: Optional[datetime] = None) -> List[ChargingSession]:
        return self._repo.list_sessions(limit=limit, since=since)