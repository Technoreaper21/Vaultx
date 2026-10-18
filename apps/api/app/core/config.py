from pydantic import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "VaultX"
    # Database URL for SQLAlchemy
    DATABASE_URL: str = "postgresql://postgres:postgres@db/vaultx"
    # For JWT
    SECRET_KEY: str = "fake-secret-key-for-demo"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days

    class Config:
        env_file = ".env"

settings = Settings()