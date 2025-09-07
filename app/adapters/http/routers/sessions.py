from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Depends
from ....application.services.session_service import SessionService
from ....adapters.memory.session_repository import InMemorySessionRepository
from ..schemas import Page, PageMeta, SessionOut
from ..deps import PageQuery, SessionFilters

def get_service() -> SessionService:
    repo = InMemorySessionRepository()
    return SessionService(repo)

router = APIRouter(prefix="/sessions", tags=["sessions"])

@router.get("", response_model=Page, summary="List charging sessions with filters")
async def list_sessions(
        page: PageQuery = Depends(),
        f: SessionFilters = Depends(),
        service: SessionService = Depends(get_service),
):
    items = service.list(limit=10_000, since=f.since)
    if f.until:
        items = [s for s in items if s.started_at < f.until]
    if f.station_id:
        items = [s for s in items if s.station_id == f.station_id]
    if f.vehicle_id:
        items = [s for s in items if s.vehicle_id == f.vehicle_id]
    if f.active_only:
        items = [s for s in items if s.ended_at is None]
    total = len(items)
    sliced = items[page.offset: page.offset + page.limit]
    data = [
        SessionOut(
            id=s.id,
            vehicle_id=s.vehicle_id,
            station_id=s.station_id,
            started_at=s.started_at.isoformat(),
            ended_at=s.ended_at.isoformat() if s.ended_at else None,
            energy_kwh=s.energy_kwh,
            cost_eur=s.cost_eur,
        ).model_dump()
        for s in sliced
    ]
    return {"data": data, "meta": PageMeta(total=total, limit=page.limit, offset=page.offset).model_dump()}
