from aiogram.dispatcher.filters.state import State, StatesGroup


class NamozState(StatesGroup):
    VILOYAT_insert = State()
    DATA = State()
    keyingi = State()
    orqaga = State()
