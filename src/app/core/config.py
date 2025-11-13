# src/app/core/config.py
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    API_BASE: str = Field("http://localhost:8000")
    LOG_LEVEL: str = Field("INFO")
    LOG_FILE: str = Field("robust.log")
    SLACK_WEBHOOK: str | None = Field(None)
    SMTP_USER: str | None = Field(None)
    SMTP_PASS: str | None = Field(None)
    DB_DSN: str | None = Field("sqlite:///./test.db")
    MONGO_URI: str | None = Field(None)            # <- ADICIONEI AQUI
    EXTERNAL_TIMEOUT: int = Field(5)

    class Config:
        env_file = ".env"

settings = Settings()
