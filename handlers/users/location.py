from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from geopy import Nominatim
from keyboards.default.buttons import cancel
from loader import dp
from states.main import NamozState


@dp.message_handler(content_types=["location"], state=NamozState.VILOYAT_insert)
async def get_user_location(message: types.Message, state: FSMContext):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lon = message.location.longitude
    lat = message.location.latitude
    geoloc = Nominatim(user_agent="GetLoc")
    locname = geoloc.reverse(f"{lat}, {lon}")
    addresss = locname.address
    await state.update_data({"lat": lat, "lon": lon, "address": addresss})
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(types.KeyboardButton(text="✅ Tasdiqlash ✅"), cancel)

    await message.answer(
        f"Ma'lumotlaringiz to'g'ri ekanligini tasdiqlang\n\nAddress:{addresss}",
        reply_markup=markup)
    await NamozState.DATA.set()
