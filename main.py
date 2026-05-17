import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers.start import router
from handlers.search import  router as search_router
from handlers.discount import router as discount_router
from handlers.free_games import router as free_games_router
from handlers.upcoming import router as upcoming_router

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(router)
dp.include_router(search_router)
dp.include_router(discount_router)
dp.include_router(free_games_router)
dp.include_router(upcoming_router)

async def main():
    print("GameX bot started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())