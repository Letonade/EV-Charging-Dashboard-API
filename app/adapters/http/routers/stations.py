from fastapi import APIRouter, Depends, HTTPException, Query
from ....application.services.station_service import StationService
from ....core.enums import StationStatus
from ....adapters.memory.station_repository import InMemoryStationRepository
from ..schemas import Page, PageMeta, StationOut, StationStatusUpdateIn
from ..deps import PageQuery

def get_service() -> StationService:
    repo = InMemoryStationRepository()
    return StationService(repo)


router = APIRouter(prefix="/stations", tags=["stations"])

@router.get("", response_model=Page, summary="List charging stations")

async def list_stations(
        page: PageQuery = Depends(),
        service: StationService = Depends(get_service),
):
    items = service.list()
    sliced = items[page.offset: page.offset + page.limit]
    data = [
        StationOut(
            id=s.id,
            name=s.name,
            latitude=s.location.latitude,
            longitude=s.location.longitude,
            status=s.status,
            connectors=s.connectors,
        ).model_dump()
        for s in sliced
    ]
    return {"data": data, "meta": PageMeta(total=len(items), limit=page.limit, offset=page.offset).model_dump()}


@router.patch("/{station_id}/status", response_model=StationOut, summary="Update station status")

async def set_status(
        station_id: str,
        payload: StationStatusUpdateIn,
        service: StationService = Depends(get_service),
):
    try:
        status = StationStatus(payload.status)
    except ValueError:
        raise HTTPException(status_code=422, detail=f"Unknown status '{payload.status}'")
    st = service.set_status(station_id, status)
    return StationOut(
        id=st.id,
        name=st.name,
        latitude=st.location.latitude,
        longitude=st.location.longitude,
        status=st.status,
        connectors=st.connectors,
    )
