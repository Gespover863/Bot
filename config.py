import logging
from aiogram import Bot, Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters.state import State, StatesGroup

logging.basicConfig(level=logging.INFO)

bot = Bot(token='1243696368:AAELUYmlXkXKuWJ8OgdchsolwBSF8VSSisw')
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

storage = {}
DELAY = 30
old_lots = []
new_lots = []
authorization_users = []


class Form(StatesGroup):
    url = State()
    max_price = State()