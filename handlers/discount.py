from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "🔥 Топ скидки")
async def start_command(message: Message):
    await message.answer(
        "Тут должны будуть появиться 10 игр со скидками,отсортированные по количеству отзывов в стиме"
    )