from pydantic import PostgresDsn, computed_field, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache



class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_HOST: str = "0.0.0.0"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "postgres"

    @computed_field
    @property
    def DATABASE_URL(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )

    JWT_SECRET_KEY: str = "default-jwt-secret"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


    APP_NAME: str = "Beshpagir Church"
    DEBUG: bool = False
    ENVIRONMENT: str = "dev"


@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()




# DATABASE_URL = env.str(
#     "DATABASE_URL",
#     default="postgresql+asyncpg://postgres:postgres@0.0.0.0:5432/postgres"
# )
#
# TEST_DATABASE_URL = env.str(
#     "DATABASE_URL",
#     default="postgresql+asyncpg://postgres-test:postgres-test@0.0.0.0:5433/postgres-test"
# )
