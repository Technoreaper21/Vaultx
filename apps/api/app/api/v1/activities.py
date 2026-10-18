from fastapi import APIRouter
from typing import List, Optional
from pydantic import BaseModel

router = APIRouter()

class Activity(BaseModel):
    id: str
    title: str
    description: str
    is_placeholder: bool = True
    source_url: Optional[str] = None

# Stub data
activities_data = [
    Activity(
        id="act1",
        title="Introduction to Coding",
        description="Learn basics of programming",
        is_placeholder=True,
        source_url=None
    ),
    Activity(
        id="act2",
        title="Science Experiment",
        description="Simple chemistry experiment",
        is_placeholder=True,
        source_url=None
    ),
    Activity(
        id="act3",
        title="Math Olympiad Training",
        description="Prepare for math competitions",
        is_placeholder=True,
        source_url=None
    ),
    Activity(
        id="act4",
        title="Creative Writing Workshop",
        description="Improve your writing skills",
        is_placeholder=True,
        source_url=None
    ),
    Activity(
        id="act5",
        title="Robotics Basics",
        description="Build simple robots",
        is_placeholder=True,
        source_url=None
    )
]

@router.get("/", response_model=List[Activity])
def get_activities():
    return activities_data