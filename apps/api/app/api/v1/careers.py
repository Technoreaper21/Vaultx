from fastapi import APIRouter
from typing import List, Optional
from pydantic import BaseModel

router = APIRouter()

class Career(BaseModel):
    id: str
    title: str
    description: str
    is_placeholder: bool = True
    source_url: Optional[str] = None

# Stub data
careers_data = [
    Career(
        id="career1",
        title="Software Developer",
        description="Build applications and systems",
        is_placeholder=True,
        source_url=None
    ),
    Career(
        id="career2",
        title="Data Analyst",
        description="Analyze data to help make decisions",
        is_placeholder=True,
        source_url=None
    ),
    Career(
        id="career3",
        title="Digital Marketing Specialist",
        description="Promote products and services online",
        is_placeholder=True,
        source_url=None
    ),
    Career(
        id="career4",
        title="Graphic Designer",
        description="Create visual content for media",
        is_placeholder=True,
        source_url=None
    ),
    Career(
        id="career5",
        title="Renewable Energy Technician",
        description="Work with solar and wind energy systems",
        is_placeholder=True,
        source_url=None
    )
]

@router.get("/", response_model=List[Career])
def get_careers():
    return careers_data