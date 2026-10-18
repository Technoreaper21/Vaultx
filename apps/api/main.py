from fastapi import FastAPI
from app.api.routers import auth, activities, careers, opportunities, sync

app = FastAPI(title="VaultX API", version="0.1.0")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(activities.router, prefix="/activities", tags=["activities"])
app.include_router(careers.router, prefix="/careers", tags=["careers"])
app.include_router(opportunities.router, prefix="/opportunities", tags=["opportunities"])
app.include_router(sync.router, prefix="/sync", tags=["sync"])


@app.get("/health")
def health():
    return {"status": "ok"}