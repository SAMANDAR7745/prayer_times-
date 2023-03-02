import asyncio
from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot
import pandas as pd


# @dp.message_handler()
# async def send_ad_to_all(message: types.Message):
#     user_id = message.from_user.id
#     try:
#         await bot.send_message(chat_id=user_id, text="kanaliga obuna bo'ling!")
#     except:
#         await message.answer(text=f"{user_id}")
