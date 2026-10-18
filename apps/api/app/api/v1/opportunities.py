from fastapi import APIRouter
from typing import List, Optional
from pydantic import BaseModel

router = APIRouter()

class Opportunity(BaseModel):
    id: str
    title: str
    description: str
    eligibility_rules: dict
    is_placeholder: bool = True
    source_url: Optional[str] = None
    last_verified_at: str  # ISO string

# Stub data
opportunities_data = [
    Opportunity(
        id="opp1",
        title="National Science Scholarship",
        description="Scholarship for students excelling in science",
        eligibility_rules={
            "min_age": 14,
            "max_age": 20,
            "min_grade": 9,
            "subjects": ["science"]
        },
        is_placeholder=True,
        source_url=None,
        last_verified_at="2026-01-01"
    ),
    Opportunity(
        id="opp2",
        title="Apprenticeship in Renewable Energy",
        description="Hands-on training in solar panel installation",
        eligibility_rules={
            "min_age": 16,
            "max_age": 25,
            "education": ["high_school", "vocational"]
        },
        is_placeholder=True,
        source_url=None,
        last_verified_at="2026-01-01"
    ),
    Opportunity(
        id="opp3",
        title="Women in Tech Mentorship",
        description="Mentorship program for girls interested in tech",
        eligibility_rules={
            "gender": ["female"],
            "min_age": 15,
            "max_age": 22
        },
        is_placeholder=True,
        source_url=None,
        last_verified_at="2026-01-01"
    )
]

@router.get("/", response_model=List[Opportunity])
def get_opportunities():
    return opportunities_data