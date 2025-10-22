from asyncio import run

from app.core.utils import async_client


async def get_all_currency_pairs() -> list[str] | None:
    async with async_client() as client:
        response = await client.get(url="/ticker/price")

    if response.status_code == 200:
        pairs_list = [currency["symbol"] for currency in response.json()]
        print(response.headers.items())
        # print(pairs_list)
        return pairs_list
    return None


async def get_pair_price(cur_pair: str) -> dict[str, str] | None:
    async with async_client() as client:
        response = await client.get(url=f"/ticker/price?symbol={cur_pair}")

    if response.status_code == 200:
        print(response.headers.items())
        print(response.json())
        return {**response.json()}
    return None


if __name__ == "__main__":
    run(get_all_currency_pairs())
    run(get_pair_price("OMGBTC"))
    # run(get_pair_price("BTCUSDT"))
    # run(get_pair_price("ETHUSDT"))
    # run(get_all_currency_pairs())
    # run(get_pair_price("ETHBTC"))
