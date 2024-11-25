"""
            ВАЖНО!!!
Для работы ТЕЛЕГРАММ-бота НЕОБХОДИМ
1. Python 3.11 <=
2. aiogram 2 (в моем случае 2.23.1)
"""

from cgitb import text

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = "7637175952:AAHgHoNsU0DlMAkIDPJ2AiWDLjxvdazRWcw"

bot = Bot(token=token)  # сам бот
dp = Dispatcher(bot)


@dp.message_handler(
    commands=["start", "go"]
)  # Декоратор для определения команды. То есть фраза начинается с /
async def start(message: types.Message) -> None:
    await message.answer(
        text=f"Привет, {message.from_user.first_name}"
    )  # процедура отправки сообщения пользователю
    await bot.send_sticker(
        chat_id=message.from_user.id,
        sticker="CAACAgIAAxkBAAENBz1nH8TyQcLHp-b6hJcG_KE6wAjjFgACPA4AAryrWEslKJiOAc6xfTYE",
    )


@dp.message_handler(content_types=["sticker"])
async def start_2(message: types.Message) -> None:
    await bot.send_photo(
        chat_id=message.chat.id,
        photo="https://avatars.mds.yandex.net/i?id=c9417a022baece07e0fee9b1e9cc827621db9b1c-8320406-images-thumbs&n=13",
        caption="Классный стикер, а я тебе отправлю фото!",
    )


@dp.message_handler(content_types=["text"])
async def start(message: types.Message) -> None:
    print(message)
    await message.answer(text=message.text)


@dp.message_handler(content_types=["photo"])
async def start_2(message: types.Message) -> None:
    await message.reply(text="Классная фотка! Лови мой стикер")
    await bot.send_sticker(
        chat_id=message.from_user.id,
        sticker="CAACAgIAAxkBAAENBz1nH8TyQcLHp-b6hJcG_KE6wAjjFgACPA4AAryrWEslKJiOAc6xfTYE",
    )


@dp.message_handler(content_types=["voice"])
async def start_4(message: types.Message) -> None:
    await message.answer(text=f"{message}")


executor.start_polling(dp, skip_updates=True)
