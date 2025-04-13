from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class SecuritySetting(BaseSettings):
    secret_key: str
    access_token_expire_minutes: int

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_security_setting() -> SecuritySetting:
    return SecuritySetting()
