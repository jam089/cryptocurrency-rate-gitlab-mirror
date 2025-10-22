from httpx import AsyncClient

from app.core import settings


def async_client() -> AsyncClient:
    client = AsyncClient(
        base_url=f"https://{settings.binance.main_url}{settings.binance.api_prefix}",
        follow_redirects=False,
        headers={"Cache-Control": "no-cache"},
    )
    return client
