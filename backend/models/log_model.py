from datetime import datetime

from pydantic import BaseModel, Field


class Log(BaseModel):
    id: int
    endpoint: str = Field(..., min_length=1)
    operation: str = Field(..., min_length=1)
    arguments: str = Field(..., min_length=1)
    result: str = Field(..., min_length=1)
    status_code: int = Field(..., ge=100, le=599)
    timestamp: datetime
