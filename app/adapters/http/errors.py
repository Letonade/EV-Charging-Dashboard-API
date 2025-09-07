from fastapi import Request
from fastapi.responses import JSONResponse
from .schemas import ErrorResponse


async def not_found_handler(request: Request, exc: KeyError):
    return JSONResponse(status_code=404, content=ErrorResponse(error="not_found", detail=str(exc)).model_dump())
