from pydantic import BaseModel, Field
from datetime import datetime

class Log(BaseModel):
    id: int
    endpoint: str = Field(..., min_length=1)
    operation: str = Field(..., min_length=1)
    arguments: str = Field(..., min_length=1)
    result: str = Field(..., min_length=1)
    status_code: int = Field(..., ge=100, le=599)
    timestamp: datetime