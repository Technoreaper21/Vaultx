from fastapi import APIRouter, Depends
from app.crud.career import get_careers
from app.schemas.career import Career
from app.db.session import get_db

router = APIRouter()

@router.get("/", response_model=list[Career])
def read_careers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    careers = get_careers(db, skip=skip, limit=limit)
    return careers
EOF