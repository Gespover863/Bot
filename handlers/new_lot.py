from aiogram import types
from aiogram.dispatcher import FSMContext

from config import dp, storage, Form


url = ''
max_price = ''


@dp.message_handler(state=Form.url)
async def add_url(message: types.Message):
    await Form.next()

    global url
    url = message.text

    await message.answer('Введите необходимую максимальную цену на лот')


@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.max_price)
async def process_age_invalid(message: types.Message):
    return await message.answer("Введите число!")


@dp.message_handler(lambda message: message.text.isdigit(), state=Form.max_price)
async def add_max_price(message: types.Message, state: FSMContext):
    global max_price

    max_price = message.text
    storage[url] = max_price

    await message.answer("Nice.")

    await state.finish()