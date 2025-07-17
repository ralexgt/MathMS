from typing import Dict

from fastapi import APIRouter, Depends, status

from services.log_service import LogService
from utils.get_log_service import get_log_service

router = APIRouter(prefix="/math")


@router.post(
    "/pow", response_model=Dict[str, str],
    status_code=status.HTTP_200_OK
)
def math_power(
    log_service: LogService = Depends(get_log_service)
):
    """Fake some math for test purposes"""
    log_service.log_request(
        "/math/pow", "pow", "2, 3", "8", status.HTTP_200_OK
    )
    return {"result": "8"}
