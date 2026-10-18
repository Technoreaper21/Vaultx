from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional
import uuid

router = APIRouter()

# In-memory storage for demo
# In reality, this would be a database
sync_store: Dict[str, Dict[str, Any]] = {}

class SyncItem(BaseModel):
    id: str  # client-generated ID
    type: str  # e.g., "activity_response", "opportunity_application"
    data: Dict[str, Any]
    client_timestamp: Optional[str] = None

class SyncResponse(BaseModel):
    status: str
    server_id: Optional[str] = None
    message: str

@router.post("/push", response_model=SyncResponse)
def push_sync(item: SyncItem):
    # Idempotent: if we have already stored this client ID, return existing
    if item.id in sync_store:
        return SyncResponse(
            status="already_exists",
            server_id=item.id,
            message="Item already synced"
        )

    # Store the item
    sync_store[item.id] = {
        "type": item.type,
        "data": item.data,
        "client_timestamp": item.client_timestamp,
        "server_timestamp": str(uuid.uuid4())  # fake server timestamp
    }

    return SyncResponse(
        status="synced",
        server_id=item.id,
        message="Item synced successfully"
    )

@router.get("/{item_id}")
def get_sync_item(item_id: str):
    if item_id not in sync_store:
        raise HTTPException(status_code=404, detail="Item not found")
    return sync_store[item_id]