from pydantic import BaseModel, Field


class FactorialRequest(BaseModel):
    number: int = Field(..., gt=0)


class FactorialResponse(BaseModel):
    result: int = Field(..., gt=0)
