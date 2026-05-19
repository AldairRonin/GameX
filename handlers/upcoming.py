from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from services.rawg_api import get_upcoming_games

router = Router()


def create_keyboard(page: int):
    buttons = []

    if page > 1:
        buttons.append(
            InlineKeyboardButton(
                text="⬅️",
                callback_data=f"upcoming_{page - 1}"
            )
        )

    buttons.append(
        InlineKeyboardButton(
            text="➡️",
            callback_data=f"upcoming_{page + 1}"
        )
    )

    return InlineKeyboardMarkup(inline_keyboard=[buttons])


@router.message(F.text == "🚀 Предстоящие игры")
async def upcoming_games(message: Message):

    page = 1
    games = await get_upcoming_games(page)

    response_text = "🚀 Предстоящие игры:\n\n"

    for game in games:
        title = game["name"]
        released = game.get("released", "Неизвестно")

        response_text += (
            f"🎮 {title}\n"
            f"📅 {released}\n\n"
        )

    await message.answer(
        response_text,
        reply_markup=create_keyboard(page)
    )


@router.callback_query(F.data.startswith("upcoming_"))
async def change_page(callback: CallbackQuery):

    page = int(callback.data.split("_")[1])

    games = await get_upcoming_games(page)

    response_text = "🚀 Предстоящие игры:\n\n"

    for game in games:
        title = game["name"]
        released = game.get("released", "Неизвестно")

        response_text += (
            f"🎮 {title}\n"
            f"📅 {released}\n\n"
        )

    await callback.message.edit_text(
        response_text,
        reply_markup=create_keyboard(page)
    )

    await callback.answer()