from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "🆓 Бесплатные игры")
async def free_games(message: Message):
    await message.answer(
        "Тут должны появиться недавние бесплатные игры"
    )