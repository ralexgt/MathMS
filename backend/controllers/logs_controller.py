from typing import List

from fastapi import APIRouter, Depends, status

from models.log_model import Log
from services.log_service import LogService
from utils.get_log_service import get_log_service

router = APIRouter(prefix="/logs")


@router.get("/", response_model=List[Log], status_code=status.HTTP_200_OK)
def read_logs(
    log_service: LogService = Depends(get_log_service)
):
    return log_service.read_logs(limit=50)
