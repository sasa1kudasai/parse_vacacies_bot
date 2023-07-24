import asyncio

from aiogram import types

from bot import dp
from parsers.vacancy_parser import parse_vacancies


@dp.message_handler(commands=['search'])
async def search_vacancies(message: types.Message):
    await message.reply("Введите запрос для поиска вакансий:")

@dp.message_handler(lambda message: message.text.startswith('/search_'))
async def process_search(message: types.Message):
    query = message.text.replace('/search_', '')
    vacancies = parse_vacancies(query)

    if vacancies:
        response = "Вот найденные вакансии:\n"
        for vacancy in vacancies:
            response += f"{vacancy['title']}\n{vacancy['link']}\n\n"

        max_message_length = 4096
        chunks = [response[i:i + max_message_length] for i in range(0, len(response), max_message_length)]
        for chunk in chunks:
            await message.reply(chunk, disable_web_page_preview=True)

            # Добавляем задержку между отправкой сообщений, чтобы не превышать ограничения на частоту отправки
            await asyncio.sleep(1)

    else:
        response = "По вашему запросу ничего не найдено."

    await message.reply(response, disable_web_page_preview=True)