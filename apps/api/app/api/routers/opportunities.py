from fastapi import APIRouter, Depends, HTTPException
from app.crud.opportunity import get_opportunities, check_eligibility
from app.schemas.opportunity import Opportunity, OpportunityEligibilityCheck
from app.db.session import get_db

router = APIRouter()

@router.get("/", response_model=list[Opportunity])
def read_opportunities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    opportunities = get_opportunities(db, skip=skip, limit=limit)
    return opportunities

@router.post("/eligibility", response_model=OpportunityEligibilityCheck)
def check_opportunity_eligibility(opportunity_id: int, db: Session = Depends(get_db)):
    # In a real app, we would get the current user from dependencies
    # For now, we'll stub with a placeholder user ID
    result = check_eligibility(db, opportunity_id=opportunity_id, user_id=1)
    return result
EOF