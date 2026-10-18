from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CareerBase(BaseModel):
    title: str
    description: str
    is_placeholder: bool = True
    source_url: Optional[str] = None
    last_verified_at: Optional[datetime] = None

class CareerCreate(CareerBase):
    pass

class CareerUpdate(CareerBase):
    pass

class Career(CareerBase):
    id: int

    class Config:
        orm_mode = True
EOF