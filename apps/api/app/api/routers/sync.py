from fastapi import APIRouter, Depends, HTTPException
from app.crud.sync import push_sync
from app.schemas.sync import SyncPush
from app.db.session import get_db

router = APIRouter()

@router.post("/push")
def push_sync_endpoint(sync_data: SyncPush, db: Session = Depends(get_db)):
    result = push_sync(db, sync_data)
    return result
EOF