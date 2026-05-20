import aiohttp

BASE_URL = "https://www.cheapshark.com/api/1.0/deals"

async def get_top_discounts(page=0):
    params = {
        "storeID": 1,
        "pageSize": 8,
        "pageNumber": page,
        "sortBy": "Deal Rating"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, params=params) as response:
            return await response.json()

async def get_free_games():
    params = {
        "storeID": 1,
        "upperPrice":0,
        "pageSize": 10,

    }

    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL,params=params) as response:
            return  await response.json()
