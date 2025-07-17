from fastapi import Depends

from models.database import Database
from services.log_service import LogService


def get_log_service(db: Database = Depends()) -> LogService:
    return LogService(db)


def log_service_errors() -> LogService:
    """
    This function is used to directly get the LogService instance
    without using dependency injection.
    """
    db = Database()
    return LogService(db)
