from os import getenv
import asyncio
from aiogram import Bot, Dispatcher
from routes import router, notifier

BOT_TOKEN=getenv("BOT_TOKEN")

dp=Dispatcher()
dp.include_router(router)

async def main():
    bot = Bot(token=BOT_TOKEN)
    print("Starting bot...")
    asyncio.create_task(notifier(bot))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())