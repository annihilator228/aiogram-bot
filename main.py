import asyncio
from aiogram import Bot, Dispatcher
from Tokens import BOT_TOKEN_Lesson8
from routes import router, notifier

BOT_TOKEN=BOT_TOKEN_Lesson8

dp=Dispatcher()
dp.include_router(router)

async def main():
    bot = Bot(token=BOT_TOKEN)
    print("Starting bot...")
    asyncio.create_task(notifier(bot))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())