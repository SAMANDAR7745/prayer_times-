import sqlite3
from states.main import NamozState
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, db, bot
from keyboards.default.buttons import location


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    user_id = message.from_user.id
    print(user_id)
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(location)
        await message.answer(f"Xush kelibsiz! {name}\nNamoz vaqtni bilish uchun\nO'zingizni joylashuvni jo'nating",
                             reply_markup=markup)
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)
        await NamozState.VILOYAT_insert.set()

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} bazaga oldin qo'shilgan")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(location)
        await message.answer(f"Xush kelibsiz! {name}\nNamoz vaqtni bilish uchun\nO'zingizni joylashuvni jo'nating",
                             reply_markup=markup)
        await NamozState.VILOYAT_insert.set()
