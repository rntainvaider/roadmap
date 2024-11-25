from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)
from aiogram.utils import executor

token = "7637175952:AAHgHoNsU0DlMAkIDPJ2AiWDLjxvdazRWcw"

bot = Bot(token=token)  # сам бот
dp = Dispatcher(bot)

box_main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)  # коробка
b1 = KeyboardButton(text="😅")  # кнопка
b2 = KeyboardButton(text="Фото")
b3 = KeyboardButton(text="Ссылки")
box_main.add(b1, b2, b3)  # кнопка

inl_box = InlineKeyboardMarkup()
inl_1 = InlineKeyboardButton(text="Ссылка 1", url="https://replit.com/")
inl_2 = InlineKeyboardButton(
    text="Ссылка 2",
    url="https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fpixy.org%2Fsrc%2F38%2F380438.jpg&lr=213&pos=3&rpt=simage&text=питон",
)
inl_box.add(inl_1, inl_2)


inl_box2 = InlineKeyboardMarkup()
inl1 = InlineKeyboardButton(text="Ссылка 1", callback_data="+")
inl2 = InlineKeyboardButton(text="Ссылка 2", callback_data="-")
inl_box2.add(inl1, inl2)


@dp.message_handler(
    commands=["start", "go"]
)  # Декоратор для определения команды. То есть фраза начинается с /
async def start(message: types.Message) -> None:
    await message.answer(
        text=f"Привет, {message.from_user.first_name}", reply_markup=box_main
    )  # процедура отправки сообщения пользователю


@dp.callback_query_handler()
async def start_3(callback: types.CallbackQuery) -> None:
    if callback.data == "+":
        await callback.answer(text="Вы нажали на плюс")
    elif callback.data == "-":
        await callback.answer(text="Вы нажали на минус")


@dp.message_handler(content_types=["text"])
async def start_3(message: types.Message) -> None:
    if message.text.lower() == "😅":
        await message.answer(text="Не волнуйся)")
    elif message.text.lower() == "ссылки":
        await message.answer(text="Нажми на кнопку!", reply_markup=inl_box2)
    else:
        await message.answer(text="Не понимаю о чем речь")
    await message.delete()


executor.start_polling(dp, skip_updates=True)
