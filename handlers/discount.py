from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from services.cheapshark_api import get_top_discounts

router = Router()


sort_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="⭐ Выгода",
                callback_data="sort_Deal Rating"
            )
        ],
        [
            InlineKeyboardButton(
                text="🆕 Новые",
                callback_data="sort_recent"
            )
        ]
    ]
)


def get_keyboard(page: int, sort_by: str):
    buttons = []

    if page > 0:
        buttons.append(
            InlineKeyboardButton(
                text="⬅️",
                callback_data=f"discount_{page - 1}_{sort_by}"
            )
        )

    buttons.append(
        InlineKeyboardButton(
            text="➡️",
            callback_data=f"discount_{page + 1}_{sort_by}"
        )
    )

    return InlineKeyboardMarkup(inline_keyboard=[buttons])


async def format_discounts(page: int, sort_by: str = "Deal Rating"):
    deals = await get_top_discounts(page, sort_by)

    response_text = "🔥 Топ скидок:\n\n"

    for game in deals:
        title = game["title"]
        sale_price = game["salePrice"]
        normal_price = game["normalPrice"]
        savings = round(float(game["savings"]))

        response_text += (
            f"🎮 {title}\n"
            f"💸 ${sale_price} (вместо ${normal_price})\n"
            f"🔥 Скидка: {savings}%\n\n"
        )

    return response_text



@router.message(F.text == "🔥 Топ скидки")
async def discount(message: Message):
    await message.answer(
        "📊 Выберите способ сортировки:",
        reply_markup=sort_keyboard
    )




@router.callback_query(F.data.startswith("sort_"))
async def choose_sort(callback: CallbackQuery):
    sort_by = callback.data[5:]

    page = 0

    text = await format_discounts(page, sort_by)

    await callback.message.edit_text(
        text,
        reply_markup=get_keyboard(page, sort_by)
    )

    await callback.answer()



@router.callback_query(F.data.startswith("discount_"))
async def paginate(callback: CallbackQuery):
    parts = callback.data.split("_")

    page = int(parts[1])
    sort_by = "_".join(parts[2:])

    text = await format_discounts(page, sort_by)

    await callback.message.edit_text(
        text,
        reply_markup=get_keyboard(page, sort_by)
    )

    await callback.answer()