from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class OpportunityBase(BaseModel):
    title: str
    description: str
    eligibility_rules: str  # JSON string
    is_placeholder: bool = True
    source_url: Optional[str] = None
    last_verified_at: Optional[datetime] = None

class OpportunityCreate(OpportunityBase):
    pass

class OpportunityUpdate(OpportunityBase):
    pass

class Opportunity(OpportunityBase):
    id: int

    class Config:
        orm_mode = True

class OpportunityEligibilityCheck(BaseModel):
    opportunity_id: int
    criteria_passed: list[dict]  # list of {criterion: str, passed: bool, explanation: str}
    overall_passed: bool
EOF