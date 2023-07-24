from bot import on_startup, dp

if __name__ == '__main__':
    from aiogram import executor
    from handlers.command_handlers import *

    executor.start_polling(dp, on_startup=on_startup)