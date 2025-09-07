from typing import Optional
from datetime import datetime
from fastapi import Query

class PageQuery:
    def __init__(
            self,
            limit: int = Query(50, ge=1, le=500, description="Max items to return"),
            offset: int = Query(0, ge=0, description="Items to skip before starting to collect the result set"),
    ):
        self.limit = limit
        self.offset = offset


class SessionFilters:
    def __init__(
            self,
            station_id: Optional[str] = Query(None, description="Filter by station id"),
            vehicle_id: Optional[str] = Query(None, description="Filter by vehicle id"),
            active_only: bool = Query(False, description="Only sessions with no end time"),
            since: Optional[datetime] = Query(None, description="Return sessions started since this UTC datetime"),
            until: Optional[datetime] = Query(None, description="Return sessions started before this UTC datetime"),
    ):
        self.station_id = station_id
        self.vehicle_id = vehicle_id
        self.active_only = active_only
        self.since = since
        self.until = until
