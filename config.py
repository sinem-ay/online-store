from pydantic import BaseSettings, PostgresDsn
from functools import lru_cache


class Settings(BaseSettings):
    db_name: str
    db_url: PostgresDsn

    class Config:
        env_file = ".envrc"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    settings = Settings()
    return settings
