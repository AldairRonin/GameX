from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "ℹ️ Help")
async def help_command(message: Message):

    help_text = (
        "🎮 <b>GameX Bot Help</b>\n\n"

        "🔥 <b>Топ скидки</b>\n"
        "Показывает текущие скидки Steam.\n\n"

        "🆓 <b>Бесплатные игры</b>\n"
        "Игры, которые временно стали бесплатными.\n\n"

        "🚀 <b>Предстоящие игры</b>\n"
        "Ожидаемые игры с датой выхода.\n\n"

        "🔍 <b>Найти игру</b>\n"
        "Введите название игры и получите:\n"
        "• постер\n"
        "• Metacritic\n"
        "• жанры\n"
        "• описание\n"
        "• Steam ссылку\n\n"
    )
    await message.answer(
        help_text,
        parse_mode="HTML"
    )