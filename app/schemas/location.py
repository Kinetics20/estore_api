from pydantic import BaseModel, Field, PositiveInt


class LocationCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    address: str = Field(..., min_length=5, max_length=200)
    capacity: PositiveInt
