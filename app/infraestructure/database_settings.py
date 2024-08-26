from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSetting(BaseSettings):
    
    database_connection: str
    async_database_connection: str

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_database_setting() -> DatabaseSetting:
    return DatabaseSetting()
