from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class BinanceApi(BaseModel):
    main_url: str = "api.binance.com"
    url_list: list[str] = [
        "api.binance.com",
        "api-gcp.binance.com",
        "api1.binance.com",
        "api2.binance.com",
        "api3.binance.com",
        "api4.binance.com",
    ]
    api_prefix: str = "/api/v3"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=[".env.template", ".env", ".env.local"],
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="fetcher__",
    )

    binance: BinanceApi = BinanceApi()


settings = Settings()
