from aiogram import Router, F
from aiogram.types import Message
from services.rawg_api import get_upcoming_games

router = Router()

@router.message(F.text == "🚀 Предстоящие игры")
async def upcoming_games(message: Message):
    games = await get_upcoming_games()

    response_text = "🚀 Предстоящие игры:\n\n"

    for game in games:
        title = game["name"]
        release_date = game["released"]
        rating = game["rating"]

        response_text += (
            f"🎮 {title}\n"
            f"📅 Выход: {release_date}\n\n"
        )

    await message.answer(response_text)

