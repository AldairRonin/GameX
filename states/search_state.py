from aiogram.fsm.state import State, StatesGroup

class SearchGameState(StatesGroup):
    waiting_for_game_name = State()