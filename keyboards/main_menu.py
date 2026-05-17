from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔥 Топ скидки"),
            KeyboardButton(text="🆓 Бесплатные игры")
        ],
        [
            KeyboardButton(text="🚀 Предстоящие игры"),
            KeyboardButton(text="🔍 Найти игру")
        ],
        [
            KeyboardButton(text="ℹ️ Help")
        ]
    ],
    resize_keyboard=True
)