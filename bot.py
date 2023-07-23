from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram import executor
import os
import logging

# Замените 'YOUR_TOKEN' на токен, полученный от BotFather
TOKEN = os.environ.get('BOT_TOKEN')
MY_TOKEN = os.environ.get('MY_TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот. Как дела?")

async def on_startup(dp):
    await bot.send_message(chat_id=MY_TOKEN, text='Бот запущен')

if __name__ == '__main__':
    from aiogram import executor
    from handlers import *  # Импортируйте обработчики команд и сообщений

    executor.start_polling(dp, on_startup=on_startup)