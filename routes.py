import asyncio
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Bot

router = Router()

subscribers = set()

async def notifier(bot: Bot):
    while True:
        if subscribers:
            for user in list(subscribers):
                try:
                    await bot.send_message(user,"Уведомление!")
                except Exception:
                    pass
        await asyncio.sleep(10)

@router.message(Command('start'))
async def start(message: Message):
    await message.answer(
        "Привет!👋\n"
        "Я могу помочь с рассылкой!\n\n"
        "Команды:\n"
        "/subscribe - Подписаться на уведомления🔔\n"
        "/unsubscribe - Отписка🔕\n"
        "/subscribers - Список подписчиков📋")

@router.message(Command('subscribe'))
async def subscribe(message: Message):
    subscribers.add(message.from_user.id)
    await message.answer("Вы подписались на уведомления!🔔")

@router.message(Command('unsubscribe'))
async def unsubscribe(message: Message):
    subscribers.discard(message.from_user.id)
    await message.answer("Вы отписались от уведомлений!🔕")

@router.message(Command('subscribers'))
async def cmd_subscribers(message: Message):
    if not subscribers:
        await message.answer('Пока никого нет!❌')
        return
    text='Подписчики:\n\n'
    for user in list(subscribers):
        text+=f"{user}\n"
    await message.answer(text)