from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from states.search_state import SearchGameState
from services.rawg_api import (
    search_game,
    get_game_details,
    get_steam_url
)


router = Router()

@router.message(F.text == "🔍 Найти игру")
async def search_start(message: Message, state: FSMContext):

    await state.set_state(SearchGameState.waiting_for_game_name)

    await message.answer(
        "🔍 Введите название игры:"
    )

@router.message(SearchGameState.waiting_for_game_name)
async def process_game_search(message: Message, state: FSMContext):

    games = await search_game(message.text)

    if not games:
        await message.answer("❌ Игра не найдена.")
        return

    game = games[0]

    title = game["name"]
    metacritic = game.get("metacritic", "N/A")
    released = game.get("released", "Неизвестно")
    genres = ", ".join(
        genre["name"] for genre in game["genres"]
    )
    details = await get_game_details(game["id"])

    steam_url = await get_steam_url(game["id"])
    if not steam_url:
        game_name = game["name"]
        steam_url = f"https://store.steampowered.com/search/?term={game_name}"

    description = details.get(
        "description_raw",
        "Описание отсутствует."
    )
    description = description[:200] + "..."

    response_text = (
        f"🎮 {title}\n"
        f"⭐ Оценка на Metacritic: {metacritic}\n"
        f"📅 Выход: {released}\n"
        f"🎯 Жанры: {genres}\n"
        f"📖 Описание: {description}"
    )

    image_url = game.get("background_image")

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🛒 Страница в Steam",
                    url=steam_url
                )
            ]
        ]
    )

    if image_url:
        await message.answer_photo(
            photo=image_url,
            caption=response_text,
            reply_markup=keyboard,
        )
    else:
        await message.answer(
            response_text,
            reply_markup=keyboard
        )

    await state.clear()