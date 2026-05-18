from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "🔍 Найти игру")
async def search(message: Message):
    await message.answer(
        "Напиши мне название игры в Steam"
    )