"""
            ВАЖНО!!!
Для работы ТЕЛЕГРАММ-бота НЕОБХОДИМ
1. Python 3.11 <=
2. aiogram 2 (в моем случае 2.23.1)
"""

import sqlite3

from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils import executor

db = sqlite3.connect("ankets.db")
sql = db.cursor()

sql.execute("""
    CREATE TABLE IF NOT EXISTS anket_table (
        name TEXT,
        age TEXT,
        info TEXT,
        photo TEXT
    )
""")
db.commit()

token = "7637175952:AAHgHoNsU0DlMAkIDPJ2AiWDLjxvdazRWcw1) Напишите программу, которая проверит, является ли число палиндромом (итеративным способом)."

storage = MemoryStorage()  # Временное хранилище данных

bot = Bot(token=token)  # сам бот
dp = Dispatcher(bot, storage=storage)  # Подключаем хранилище к боту

inl_box = ReplyKeyboardMarkup()
inl_exit = KeyboardButton(text="Выйти")
inl_box.add(inl_exit)


class SetData(StatesGroup):  # новое МАШИННОЕ состояние
    name = State()
    age = State()
    info = State()
    photo = State()


@dp.message_handler(content_types=["text"], state=SetData.name)
async def start(message: types.Message, state: FSMContext):
    if message.text == "Выйти":
        await message.answer(text="ПРИНУДИТЕЛЬНОЕ ЗАВЕРШЕНИЕ РАБОТЫ")
        await state.finish()
    else:
        if message.text.isalpha():
            async with state.proxy() as data:
                data["Имя"] = message.text
                await message.answer(text=f"Рад знакомству, {message.text}", reply_markup=inl_box)
                await message.answer(text="А сколько тебе лет ?", reply_markup=inl_box)
                await SetData.next()
        else:
            await message.answer(text="Напишите корректное имя")


@dp.message_handler(content_types=["text"], state=SetData.info)
async def start(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["Инфо"] = message.text
        await message.answer(text="Очень интересно!")
        await message.answer(text="Пришли свою фотографию", reply_markup=inl_box)
        await SetData.next()


@dp.message_handler(content_types=["text"], state=SetData.age)
async def start(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data["Возраст"] = message.text
            if int(message.text) >= 18:
                await message.answer(text="А ты взрослый!")
            else:
                await message.answer(text="А ты еще очень молод!")
            await message.answer(text="Расскажи немного о себе", reply_markup=inl_box)
            await SetData.next()
    else:
        await message.answer(text="Напишите корректный вовзраст")


@dp.message_handler(content_types=["photo"], state=SetData.photo)
async def start(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["Фото"] = message.photo[0].file_id
        sql.execute(
            "INSERT INTO anket_table VALUES (?, ?, ?, ?)",
            (f'{data["Имя"]}', f'{data["Возраст"]}', f'{data["Инфо"]}', f'{data["Фото"]}'),
        )
        db.commit()
        await SetData.next()


@dp.message_handler(content_types=["text"], state=SetData.photo)
async def start(message: types.Message, state: FSMContext):
    await message.answer(text="Пришлите фотографию!!!!", reply_markup=inl_box)


@dp.message_handler(
    commands=["anketa"]
)  # Декоратор для определения команды. То есть фраза начинается с /
async def start(message: types.Message):  # Аннотация
    await message.answer(text="Давай знакомится!")  # процедура отправки сообщения пользователю
    await message.answer(text="Как тебя зовут?")  # процедура отправки сообщения пользователю
    await SetData.name.set()


@dp.message_handler(
    commands=["get_info"]
)  # Декоратор для определения команды. То есть фраза начинается с /
async def start(message: types.Message):
    sql.execute("""select * from anket_table """)
    data = sql.fetchall()
    for person in data:
        personal_data = f"Тебя зовут, {person[0]}, твой возраст {person[1]}. О тебе : {person[2]}"
        await bot.send_photo(chat_id=message.chat.id, photo=person[3], caption=personal_data)


@dp.message_handler(
    commands=["start", "go"]
)  # Декоратор для определения команды. То есть фраза начинается с /
async def start(message: types.Message):  # Аннотация
    await message.answer(
        text=f"Привет, {message.from_user.first_name}"
    )  # процедура отправки сообщения пользователю
    await bot.send_sticker(
        chat_id=message.from_user.id,
        sticker="CAACAgIAAxkBAAENBzRnH8TO1uN78--bu61Bc_-O0XE7UAACWhYAAqNwwUukoL0mWBCCZzYE",
    )


@dp.message_handler(content_types=["text"])
async def start(message: types.Message):
    await message.answer(text=message.text)


executor.start_polling(dp, skip_updates=True)
