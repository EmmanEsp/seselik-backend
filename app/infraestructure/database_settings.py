from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSetting(BaseSettings):
    
    database_url: str
    async_database_url: str

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_database_setting() -> DatabaseSetting:
    return DatabaseSetting()
