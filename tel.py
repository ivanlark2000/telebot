from aiogram import Bot, Dispatcher, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils import executor
from aiogram.utils.markdown import text

from Get_text import get_text
from config import TOKEN, list_of_text_in_base

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

button_hi = KeyboardButton('Привет! 👋')
button_fact = KeyboardButton('Факт')
greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)
button1 = KeyboardButton('Про Армию')
button2 = KeyboardButton('Про семью')
button3 = KeyboardButton('Про ВОВ')
button4 = KeyboardButton('Афоризмы')
button5 = KeyboardButton('Про друзей')
button6 = KeyboardButton('Про дорогу')
button7 = KeyboardButton('Про милицию')
button8 = KeyboardButton('Про иностранцев')
button9 = KeyboardButton('Черный Юмор')
button10 = KeyboardButton('Про студентов')
button11 = KeyboardButton('Про наркаманов')
button12 = KeyboardButton('Медецинские')
button13 = KeyboardButton('️Сказочные')
button14 = KeyboardButton('Про штирлица')
button15 = KeyboardButton('Про школу')
button16 = KeyboardButton('Про рекламу')
button17 = KeyboardButton('Про тещу')
button18 = KeyboardButton('Про криминал')
button19 = KeyboardButton('Про евреев')
button20 = KeyboardButton('Про сисадминов')
button21 = KeyboardButton('Про программистов')
button22 = KeyboardButton('Старые и бородатые')
button23 = KeyboardButton('Про бухгалтеров')
button24 = KeyboardButton('Про Била Гейтса')
button25 = KeyboardButton('Пошлые')
button26 = KeyboardButton('Про геншин')
button27 = KeyboardButton('Разные')
button28 = KeyboardButton('️Про чукчей')
button29 = KeyboardButton('Про вовочку')
button30 = KeyboardButton('Про новых русских')
button31 = KeyboardButton('Про шоу бизнес')
button32 = KeyboardButton('Народные')
button33 = KeyboardButton('Советские')
button34 = KeyboardButton('Цитаты')
button35 = KeyboardButton('Про Ржевского')
button36 = KeyboardButton('Про компьютеры')
button37 = KeyboardButton('Про кино')
button38 = KeyboardButton('Про животных')
button39 = KeyboardButton('Политические')
button40 = KeyboardButton('X-files')

markup1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2).add(button3).add(
    button4) \
    .add(button5).add(button6).add(button7).add(button8).add(button9).add(button10).add(button11).add(button12).add(
    button13) \
    .add(button14).add(button15).add(button16).add(button17).add(button18).add(button19).add(button20).add(
    button21).add(button22) \
    .add(button23).add(button24).add(button25).add(button26).add(button27).add(button28).add(button29).add(
    button30).add(button31) \
    .add(button32).add(button33).add(button34).add(button35).add(button36).add(button37).add(button38).add(
    button39).add(button40)

start_message = text(
    "/start - приветствие",
    "/anek - выбрать анекдот",
    "/fact - узнать интересные факты",
    "/Wiki - задать вопрос на Вики",
    "/cripto - получить курс крипты",
    "/doll - получить курс валют",
    "/help - помощь",
    "/info - информация о боте",
    sep="\n"
)
info_message = (
    "История противостояния солдата Дмитрия Глотова и киборга-терминатора, прибывших в 1984-й год из "
    "пост-апокалиптического будущего, "
    "где миром правят машины-убийцы, а человечество находится на грани вымирания."
)
help_message = ("Здравствуйте,!\nСпасибо, что используете наше приложение!\nМы еще не добавили <такую фичу>. Но "
                "я думаю, это крутая идея! С ней определенно <тут напишите, почему это было бы здорово внедрить>.\nМы "
                "не работаем над этим в данный момент, но я отправлю вашу идею команде, посмотрим, "
                "что они скажут.\nЕсли у вас есть какие-либо другие вопросы, просто дайте мне знать, и я буду рад "
                "помочь. Хорошего вам вторника!\nДимон Глотов продакшн,\nСлужба поддержки клиентов "
                )


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(start_message)


@dp.message_handler(commands=['anek'])
async def process_start_command(message: types.Message):
    await message.reply("Выбирай что по душе", reply_markup=markup1)


if 'Про армию':
    key_dict = "pro-armiu"
    send_text = get_text(key_dict)[2]


@dp.message_handler(commands=['info'])
async def process_help_command(message: types.Message):
    await message.reply(info_message)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(help_message)


if __name__ == '__main__':
    executor.start_polling(dp)
