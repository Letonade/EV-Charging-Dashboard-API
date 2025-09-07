from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class AppSettings(BaseSettings):
    app_name: str = Field(default="EV Charging Dashboard API")
    environment: str = Field(default="dev")
    debug: bool = Field(default=True)
    use_in_memory: bool = Field(default=True)
    model_config = SettingsConfigDict(env_file=".env", env_prefix="APP_")

settings = AppSettings()
