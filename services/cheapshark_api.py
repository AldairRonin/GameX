import aiohttp

BASE_URL = "https://www.cheapshark.com/api/1.0/deals"

async def get_top_discounts(page=0, sort_by="Deal Rating"):
    params = {
        "storeID": 1,
        "pageSize": 8,
        "pageNumber": page,
        "sortBy": sort_by
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, params=params) as response:
            data = await response.json()
            if not isinstance(data, list):
                return []
            return data

async def get_free_games():
    params = {
        "storeID": 1,
        "upperPrice": 0,
        "pageSize": 10,
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, params=params) as response:
            data = await response.json()
            if not isinstance(data, list):
                return []
            return data