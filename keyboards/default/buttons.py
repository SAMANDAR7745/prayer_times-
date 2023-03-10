from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import db

back_btn = KeyboardButton(text="ORQAGA âŠī¸")



def make_products_markup(viloyat_id):
    products = db.select_all_products(viloyat_id=viloyat_id)
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(back_btn)
    for product in products:
        markup.insert(KeyboardButton(text=product[1]))
    return markup


location=KeyboardButton(text="đ Joylashuvni yuborish",request_location=True)
cancel=KeyboardButton(text="â Bekor qilish â")
back_btn = KeyboardButton(text="ORQAGA âŠī¸")