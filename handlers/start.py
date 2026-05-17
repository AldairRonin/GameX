from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards.main_menu import main_keyboard


router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        "GameX Запущен!\n\n",
        reply_markup = main_keyboard
    )