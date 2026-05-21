from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from services.cheapshark_api import get_top_discounts

router = Router()


def get_keyboard(page: int):
    buttons = []

    if page > 0:
        buttons.append(
            InlineKeyboardButton(
                text="⬅️",
                callback_data=f"discount_{page - 1}"
            )
        )

    buttons.append(
        InlineKeyboardButton(
            text="➡️",
            callback_data=f"discount_{page + 1}"
        )
    )

    return InlineKeyboardMarkup(inline_keyboard=[buttons])


async def format_discounts(page: int):
    deals = await get_top_discounts(page)

    response_text = "🔥 Топ скидок:\n\n"

    for game in deals:
        title = game["title"]
        sale_price = float(game["salePrice"])
        normal_price = float(game["normalPrice"])
        savings = round(float(game["savings"]))
        kz_sale = round(sale_price * 471)
        kz_normal = round(normal_price * 471)

        response_text += (
            f"🎮 {title}\n"
            f"💸 ₸{kz_sale} (вместо ₸{kz_normal})\n"
            f"🔥 Скидка: {savings}%\n\n"
        )

    return response_text


@router.message(F.text == "🔥 Топ скидки")
async def discount(message: Message):
    page = 0

    text = await format_discounts(page)

    await message.answer(
        text,
        reply_markup=get_keyboard(page)
    )


@router.callback_query(F.data.startswith("discount_"))
async def paginate(callback: CallbackQuery):
    page = int(callback.data.split("_")[1])

    text = await format_discounts(page)

    await callback.message.edit_text(
        text,
        reply_markup=get_keyboard(page)
    )

    await callback.answer()