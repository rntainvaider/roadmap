import sqlite3

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

db = sqlite3.connect("data.db")  # создание и подключение к БД
cursor = db.cursor()  # механизм для отправки запросов к БД

# создаем таблицу
cursor.execute(""" CREATE TABLE IF NOT EXISTS
                first_table (
                            name TEXT,
                            photo TEXT
                            )""")

db.commit()

token = "7637175952:AAHgHoNsU0DlMAkIDPJ2AiWDLjxvdazRWcw"

bot = Bot(token=token)  # сам бот
dp = Dispatcher(bot)


@dp.message_handler(
    commands=["start", "go"]
)  # Декоратор для определения команды. То есть фраза начинается с /
async def start(message: types.Message):
    await message.answer(text=f"Привет, {message.from_user.first_name}")


@dp.message_handler(content_types=["photo"])
async def start(message: types.Message) -> None:
    print(message)
    cur_photo = message.photo[0].file_id
    cur_name = message.from_user.first_name
    cursor.execute("""INSERT INTO first_table VALUES (?, ?)""", (cur_name, cur_photo))
    db.commit()


executor.start_polling(dp, skip_updates=True)
