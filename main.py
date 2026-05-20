import asyncio
import requests
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command


TOKEN = "8839155453:AAFoSKULWHO7bB1HartmGkGJ8BVroyB4VU4"
bot = Bot(token=TOKEN)
dp = Dispatcher()


def get_random_waifu():
    response = requests.get("https://nekos.best/api/v2/waifu")
    data = response.json()
    return data['results'][0]['url']

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Напиши 'хочу фото', и я пришлю картинку.")

@dp.message(Command("waifu"))
async def send_foto(message: types.Message):
    url = get_random_waifu()
    await message.answer_photo(photo=url, caption="Вот твоя картинка!")

async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())