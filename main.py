import asyncio

from config import dp, Form, DELAY, new_lots, authorization_users, storage
from aiogram import executor, types

from handlers import new_lot
from handlers.search_lots import search_lots


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    poll_keyboard.add(types.KeyboardButton(text="Запустить меня"))
    poll_keyboard.add(types.KeyboardButton(text="Добавить лот для отслеживания"))
    poll_keyboard.add(types.KeyboardButton(text="Количество лотов"))
    poll_keyboard.add(types.KeyboardButton(text="Удалить все лоты"))

    await message.answer('Jo-Jo', reply_markup=poll_keyboard)


@dp.message_handler(lambda message: message.text == "ZoF81Ew5MhAP")
async def add_lot(message: types.Message):
    authorization_users.append(message.from_user.id)

    await message.answer('Nice')


@dp.message_handler(lambda message: message.text == "Количество лотов")
async def add_lot(message: types.Message):
    if message.from_user.id in authorization_users:
        await message.answer(f'Количество записанных лотов на данный момент: {len(storage)}')


@dp.message_handler(lambda message: message.text == "Удалить все лоты")
async def add_lot(message: types.Message):
    if message.from_user.id in authorization_users:
        storage.clear()

        await message.answer('Все лоты были удалены')


@dp.message_handler(lambda message: message.text == "Запустить меня")
async def action_cancel(message: types.Message):
    if message.from_user.id in authorization_users:
        await message.answer("Поехали")

        while True:
            asyncio.ensure_future(search_lots(), loop=loop)

            if new_lots:
                for new_lot in new_lots:
                    new_lots.remove(new_lot)

                    await message.answer(new_lot)

            await asyncio.sleep(DELAY)


@dp.message_handler(lambda message: message.text == "Добавить лот для отслеживания")
async def add_lot(message: types.Message):
    if message.from_user.id in authorization_users:
        await Form.url.set()

        await message.answer('Введите ссылку на лот')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, loop=loop)
