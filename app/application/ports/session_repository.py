from typing import List, Optional
from datetime import datetime
from ...core.entities import ChargingSession


class SessionRepository:
    def list_sessions(self, *, limit: int = 50, since: Optional[datetime] = None) -> List[ChargingSession]:
        raise NotImplementedError
