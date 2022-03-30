from aiogram import Bot, Dispatcher, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils import executor
from aiogram.utils.markdown import text

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

button_hi = KeyboardButton('Привет! 👋')
button_fact = KeyboardButton('Факт')
greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)
help_message = text(
    "/start - приветствие",
    "/hi1 - авто размер",
    "/hi2 - скрыть после нажатия",
    "/hi3 - больше кнопок",
    "/hi4 - кнопки в ряд",
    "/hi5 - больше рядов",
    "/hi6 - запрос локации и номера телефона",
    "/hi7 - все методы"
    "/rm - убрать шаблоны",
    "/1 - первая кнопка",
    "/2 - сразу много кнопок",
    sep="\n"
)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    from test import greet_kb1
    await message.reply("Привет!\nНапиши мне что-нибудь!", reply_markup=greet_kb1)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(help_message)


if __name__ == '__main__':
    executor.start_polling(dp)
