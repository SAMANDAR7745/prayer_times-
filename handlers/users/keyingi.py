from datetime import datetime

import requests
from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from keyboards.inline.Buttons import keyingi_kun
from loader import dp
from states.main import NamozState

x = datetime.now()
d = x.strftime("%d")
l = int(d)
soat = x.strftime("%p")


@dp.callback_query_handler(state=NamozState.orqaga, text="orqaga")
async def get_user_location(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    addresss = data.get("address")
    url = f"http://api.aladhan.com/v1/calendarByAddress?address={addresss}&"
    response = requests.get(url)
    help1 = response.json()
    help2 = help1.get('data')[l - 1]['timings']
    # hjh = json.dumps(help1, indent=4)
    a = help1.get('data')[l - 1]['date']['readable']
    matin = f"Bugungi sana: {a}\n\nHijri sana: {help1.get('data')[l - 1]['date']['hijri']['date']}\n\nVaqt zonasi: {help1.get('data')[l]['meta']['timezone']}\n\nTong: {help2['Fajr'][0:5]}\n\nQuyosh: {help2['Sunrise'][0:5]}\n\nPeshin: {help2['Dhuhr'][0:5]}\n\nAsr: {help2['Asr'][0:5]}\n\nShom: {help2['Sunset'][0:5]}\n\nXufton: {help2['Isha'][0:5]}"

    if soat == "PM":
        with open("data/imag12es.jpeg", 'rb') as file:
            await call.message.answer_photo(photo=file,
                                            caption=matin, reply_markup=keyingi_kun)
    else:
        with open("data/islam-1.jpg", 'rb') as file:
            await call.message.answer_photo(photo=file,
                                            caption=matin, reply_markup=keyingi_kun)
            import asyncio
            import time

            async def say_after(delay, what):
                await asyncio.sleep(delay)
                print(what)

            async def main():
                print(f"started at {time.strftime('%X')}")

                await say_after(1, 'hello')
                await say_after(2, 'world')

                print(f"finished at {time.strftime('%X')}")

            asyncio.run(main())
    await NamozState.keyingi.set()
