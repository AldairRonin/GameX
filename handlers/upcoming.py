from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import date

from services.rawg_api import get_upcoming_games

router = Router()


def get_keyboard(page: int):
    buttons = []

    if page > 1:
        buttons.append(
            InlineKeyboardButton(
                text="⬅️",
                callback_data=f"page_{page - 1}"
            )
        )

    buttons.append(
        InlineKeyboardButton(
            text="➡️",
            callback_data=f"page_{page + 1}"
        )
    )

    return InlineKeyboardMarkup(inline_keyboard=[buttons])


def days_until(release_str: str) -> str:
    try:
        release_date = date.fromisoformat(release_str)
        delta = (release_date - date.today()).days
        if delta == 0:
            return "🟢 Выходит сегодня!"
        elif delta > 0:
            return f"⏳ Через {delta} дн."
        else:
            return ""
    except Exception:
        return ""


async def format_games(page: int):
    games = await get_upcoming_games(page)

    text = "🚀 Предстоящие игры:\n\n"

    for game in games:
        title = game["name"]
        released = game.get("released", "Неизвестно")
        countdown = days_until(released) if released != "Неизвестно" else ""

        text += f"🎮 {title}\n📅 {released}  {countdown}\n\n"

    return text


@router.message(F.text == "🚀 Предстоящие игры")
async def show_upcoming(message: Message):
    page = 1

    text = await format_games(page)

    await message.answer(
        text,
        reply_markup=get_keyboard(page)
    )


@router.callback_query(F.data.startswith("page_"))
async def paginate(callback: CallbackQuery):
    page = int(callback.data.split("_")[1])

    text = await format_games(page)

    await callback.message.edit_text(
        text,
        reply_markup=get_keyboard(page)
    )

    await callback.answer()