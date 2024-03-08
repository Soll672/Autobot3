import asyncio

from random import choice
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import logging

load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    logging.info(message.from_user)
    await message.answer(f"привет, {message.from_user.first_name}")


@dp.message(Command("myinfo"))
async def my_info(message: types.Message):
    user = message.from_user
    await message.answer(f" id: {user.id}\n имя: {user.first_name}\n username: {user.username}")


@dp.message(Command("sendphoto"))
async def send_photo(message: types.Message):
    photos = ['Images/1.jpg', 'Images/2.jpg', 'Images/3.jpg', 'Images/4.jpg']
    chosen_photo_path = choice(photos)
    chosen_photo = types.InputFile(chosen_photo_path)
    await bot.send_photo(message.from_user.id, chosen_photo)


@dp.message()
async def echo(message: types.Message):
    await message.answer("привет")
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
