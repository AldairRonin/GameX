import aiohttp
from config import RAWG_API_KEY

BASE_URL = "https://api.rawg.io/api/games"

async def get_upcoming_games():

    params = {
        "key": RAWG_API_KEY,
        "dates": "2026-05-18,2027-12-31",
        "ordering": "-added",
        "page_size": 10
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, params=params) as response:
            data = await response.json()
            return data["results"]