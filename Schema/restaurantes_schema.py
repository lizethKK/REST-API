from pydantic import BaseModel
from typing import Optional
import uuid


class schema(BaseModel):
    id: Optional[uuid.UUID]
    rating: int
    name: str
    site: str
    email: str
    phone: int
    street: str
    city: str
    state: str
    lat: float
    lng: float

