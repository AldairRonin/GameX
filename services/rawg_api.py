import aiohttp
from config import RAWG_API_KEY

BASE_URL = "https://api.rawg.io/api/games"

async def get_upcoming_games(page=1):

    params = {
        "key": RAWG_API_KEY,
        "dates": "2025-01-01,2026-12-31",
        "ordering": "released",
        "page_size": 5,
        "page": page
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, params=params) as response:
            data = await response.json()
            return data["results"]

async def search_game(game_name):

    params = {
        "key": RAWG_API_KEY,
        "search": game_name,
        "page_size": 1
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, params=params) as response:
            data = await response.json()
            return data["results"]

async def get_game_details(game_id):

    url = f"{BASE_URL}/{game_id}"

    params = {
        "key": RAWG_API_KEY
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            return await response.json()
