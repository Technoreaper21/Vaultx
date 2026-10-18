from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    role: str  # student, facilitator, mentor, admin

@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest):
    # Stub: return a fake token based on username
    if request.username == "student":
        role = "student"
    elif request.username == "facilitator":
        role = "facilitator"
    elif request.username == "mentor":
        role = "mentor"
    else:
        role = "admin"
    return TokenResponse(
        access_token="fake-token",
        token_type="bearer",
        role=role
    )