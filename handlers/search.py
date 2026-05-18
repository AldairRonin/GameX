from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.search_state import SearchGameState
from services.rawg_api import search_game

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
    rating = game["rating"]
    released = game["released"]

    response_text = (
        f"🎮 {title}\n"
        f"⭐ Оценка: {rating}\n"
        f"📅 Выход: {released}"
    )

    await message.answer(response_text)

    await state.clear()