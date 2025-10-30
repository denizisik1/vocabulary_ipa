from typing import Optional
import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

_env = os.environ.get("APP_ENV", "development")
load_dotenv(dotenv_path=f".env.{_env}", override=True)

class Settings(BaseSettings):
    env: str = _env
    debug: bool = _env != "production"
    database_url: str
    redis_url: Optional[str] = None
    log_level: str = "INFO"
    model_config = SettingsConfigDict(env_prefix="APP_")

settings = Settings()
