from aiogram import Router, F
from aiogram.types import Message
from services.cheapshark_api import get_top_discounts

router = Router()

@router.message(F.text == "🔥 Топ скидки")
async def start_command(message: Message):

    deals = await get_top_discounts()
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


    await message.answer(response_text)