import os
from pathlib import Path

import speech_recognition as sr
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from gtts import gTTS
from pydub import AudioSegment

token = "7637175952:AAHgHoNsU0DlMAkIDPJ2AiWDLjxvdazRWcw"

bot = Bot(token=token)  # сам бот
dp = Dispatcher(bot)
r = sr.Recognizer()


def conv(text) -> None:
    data = "new_voice.mp3"
    sp = gTTS(text=text, lang="en", slow=False)
    sp.save(data)
    Path(f"output2").mkdir(parents=True, exist_ok=True)
    AudioSegment.from_mp3(data).export("output2/new_voice.ogg", format="ogg")


def ogg_to_vaw():
    print(os.listdir("Голосовые"))  # получаем содержимое папки с голосовыми
    last_voice = os.listdir("Голосовые")[-1]  # берем последнее из списка
    print(last_voice)  # выводим его название, что бы убедится в этом
    file = os.path.abspath(
        f"Голосовые/{last_voice}"
    )  # формируем путь до последнего голосового сообщения
    Path(f"output").mkdir(parents=True, exist_ok=True)  # создаем папку если ее нет
    mp = AudioSegment.from_file(file).export(
        "file", format="mp3"
    )  # делаем копию в новую папку формата mp3
    sound = AudioSegment.from_mp3(mp)  # из mp3 конвертируем в wav
    sound.export(f"output/res.wav", format="wav")

    message = sr.AudioFile("output/res.wav")  #
    with message as source:  # считываем из аудио текст
        audio = r.record(source)
    result = r.recognize_google(
        audio, language="ru_RU"
    )  #   используя возможности библиотеки распознаем текст, так же тут можно изменять язык распознавания
    print(result)
    return result  # отправляем полученный текст из голосового


@dp.message_handler(
    content_types=["voice"]
)  # Декоратор для определения команды. То есть фраза начинается с /
async def start(message: types.Message):
    voice = await message.voice.get_file()  # получаем голосовое
    path = "Голосовые"  # название папки в которую будем скачивать голосовое
    Path(f"{path}").mkdir(parents=True, exist_ok=True)  # создается папка если ее нет
    await bot.download_file(
        file_path=voice.file_path, destination=f"{path}/voice_{len(os.listdir(path))}.ogg"
    )  #
    text = ogg_to_vaw()
    await message.answer(text=f"{message.chat.first_name} в твоем голосовом сообщении такой текст")
    await message.answer(text=f"{text} ")


@dp.message_handler(
    content_types=["text"]
)  # Декоратор для определения команды. То есть фраза начинается с /
async def start(message: types.Message):
    cur_text = message.text
    conv(cur_text)
    with open("output2/new_voice.ogg", "rb") as file:
        file_data = file.read()
        print(file_data)
    await bot.send_voice(chat_id=message.chat.id, voice=file_data)


executor.start_polling(dp, skip_updates=True)
