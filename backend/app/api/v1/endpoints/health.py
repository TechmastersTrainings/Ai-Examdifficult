"""Health check and diagnostics endpoint."""

import platform
import sys
from fastapi import APIRouter
from backend.app.core.config import settings
from backend.app.schemas.health import HealthResponse

router = APIRouter()


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="System Health & Diagnostic Check",
    description="Returns live system diagnostics, environment status, and service health.",
)
async def check_health() -> HealthResponse:
    """Return genuine operational status of the service."""
    return HealthResponse(
        status="ok",
        project_name=settings.PROJECT_NAME,
        version=settings.VERSION,
        environment=settings.ENVIRONMENT,
        system_info={
            "python_version": sys.version.split()[0],
            "platform": platform.platform(),
            "debug_mode": settings.DEBUG,
        },
        database_status="pending_phase_3",
    )
