from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ActivityBase(BaseModel):
    title: str
    description: str
    is_placeholder: bool = True
    source_url: Optional[str] = None
    last_verified_at: Optional[datetime] = None

class ActivityCreate(ActivityBase):
    pass

class ActivityUpdate(ActivityBase):
    pass

class Activity(ActivityBase):
    id: int

    class Config:
        orm_mode = True
EOF