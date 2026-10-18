from fastapi import APIRouter, Depends, HTTPException
from app.crud.activity import get_activities
from app.schemas.activity import Activity
from app.db.session import get_db

router = APIRouter()

@router.get("/", response_model=list[Activity])
def read_activities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    activities = get_activities(db, skip=skip, limit=limit)
    return activities
EOF