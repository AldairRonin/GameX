from aiogram import Router, F
from aiogram.types import Message
from services.cheapshark_api import get_free_games

router = Router()

@router.message(F.text == "🆓 Бесплатные игры")
async def free_games(message: Message):
    games = await get_free_games()
    if not games:
        await message.answer("🆓 Сейчас бесплатных игр не найдено.")
        return

    response_text = "🆓 Бесплатные игры:\n\n"

    for game in games:
        title = game["title"]
        normal_price = game["normalPrice"]

        response_text += (
            f"🎮 {title}\n"
            f"💸 Было: ${normal_price}\n"
            f"🆓 Сейчас бесплатно!\n\n"
        )
    await message.answer(response_text)