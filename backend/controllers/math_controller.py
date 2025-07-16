from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from services.log_service import LogService
from models.log_model import Log
from models.database import Database

router = APIRouter(prefix="/math")

@router.post("/pow", response_model=List[Log], status_code=status.HTTP_200_OK) 
def math_power():
    """Fake some math for test purposes"""
    db = Database()
    logger = LogService(db)
    logger.log_request("/math/pow", "pow", "2, 3", "8", status.HTTP_200_OK)
    return logger.read_logs()