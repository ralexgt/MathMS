from fastapi import Depends

from models.database import Database
from services.log_service import LogService


def get_log_service(db: Database = Depends()) -> LogService:
    return LogService(db)
