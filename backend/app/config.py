from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Chronicles"
    app_env: str = "development"
    debug: bool = True

    database_url: str
    telegram_bot_token: str
    secret_key: str

    cors_origins: str = "http://localhost:8080"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    @property
    def cors_origin_list(self) -> list[str]:
        return [
            origin.strip()
            for origin in self.cors_origins.split(",")
            if origin.strip()
        ]
settings = Settings()