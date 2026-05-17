from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔥 Top Discounts"),
            KeyboardButton(text="🆓 Free Games")
        ],
        [
            KeyboardButton(text="🚀 Upcoming Games"),
            KeyboardButton(text="🔍 Search Game")
        ],
        [
            KeyboardButton(text="❤️ Favorites"),
            KeyboardButton(text="ℹ️ Help")
        ]
    ],
    resize_keyboard=True
)