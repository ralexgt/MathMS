from typing import List

from pydantic import BaseModel, Field


class FibonacciRequest(BaseModel):
    number: int = Field(..., gt=0)


class FibonacciResponse(BaseModel):
    result: List[int] = Field(...)
