from aiogram import Bot, Dispatcher, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils import executor
from aiogram.utils.markdown import text
from Get_text import get_text
from config import TOKEN
from pars import evro, dollar
import threading

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

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
button32 = KeyboardButton('Про алкоголиков')
button33 = KeyboardButton('Про детей')
button34 = KeyboardButton('Про судей')
button35 = KeyboardButton('Народные')
button36 = KeyboardButton('Советские')
button37 = KeyboardButton('Цитаты')
button38 = KeyboardButton('Про Ржевского')
button39 = KeyboardButton('Про компьютеры')
button40 = KeyboardButton('Про кино')
button41 = KeyboardButton('Про животных')
button42 = KeyboardButton('Политические')
button43 = KeyboardButton('X-files')
button44 = KeyboardButton('Про мужчин')

markup1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2).add(button3) \
    .add(button4).add(button5).add(button6).add(button7).add(button8).add(button9).add(button10).add(button11) \
    .add(button12).add(button13).add(button14).add(button15).add(button16).add(button17).add(button18).add(button19) \
    .add(button20).add(button21).add(button22).add(button23).add(button24).add(button25).add(button26).add(button27) \
    .add(button28).add(button29).add(button30).add(button31).add(button32).add(button33).add(button34).add(button35) \
    .add(button36).add(button37).add(button38).add(button39).add(button40).add(button41).add(button42).add(button43)

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


@dp.message_handler(commands=['doll'])
async def process_start_command(message: types.Message):
    await message.reply(f"Сейчас курс: \n 1 евро = {evro.__dict__['current_converted_price']}\
     \n 1 доллар = {dollar.__dict__['current_converted_price']}")


@dp.message_handler(regexp= 'Про армию')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-armiu')[2])


@dp.message_handler(regexp= 'Цитаты')
async def msg_handler(message: types.Message):
    await message.reply(get_text('tsitati')[2])


@dp.message_handler(regexp= 'Афоризмы')
async def msg_handler(message: types.Message):
    await message.reply(get_text('aforizmi')[2])


@dp.message_handler(regexp= 'Про ВОВ')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-wow')[2])


@dp.message_handler(regexp= 'Про друзей')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-druzey')[2])


@dp.message_handler(regexp= 'Про дорогу')
async def msg_handler(message: types.Message):
    await message.reply(get_text('dorognie-pro-dorogu')[2])


@dp.message_handler(regexp= 'Про милицию')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-militsiyu')[2])


@dp.message_handler(regexp= 'Про иностранцев')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-inostrantsev')[2])


@dp.message_handler(regexp= 'Черный Юмор')
async def msg_handler(message: types.Message):
    await message.reply(get_text('cherniy-yumor')[2])


@dp.message_handler(regexp= 'Про студентов')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-studentov')[2])


@dp.message_handler(regexp= 'Про наркоманов')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-narkomanov')[2])


@dp.message_handler(regexp= 'Медецинские')
async def msg_handler(message: types.Message):
    await message.reply(get_text('meditsinskie')[2])



@dp.message_handler(regexp= '️Сказочные')
async def msg_handler(message: types.Message):
    await message.reply(get_text('skazochnie')[2])


@dp.message_handler(regexp= 'Про штирлица')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-shtirlitsa')[2])


@dp.message_handler(regexp= 'Про школу')
async def msg_handler(message: types.Message):
    await message.reply(get_text('shkolnie-i-pro-shkolu')[2])


@dp.message_handler(regexp='Про рекламу')
async def msg_handler(message: types.Message):
    await message.reply(get_text('Pro-reklamu')[2])


@dp.message_handler(regexp= 'Про тещу')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-teshu')[2])


@dp.message_handler(regexp= 'Про криминал')
async def msg_handler(message: types.Message):
    await message.reply(get_text('kriminalnie')[2])


@dp.message_handler(regexp= 'Про евреев')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-evreev')[2])


@dp.message_handler(regexp= 'Про сисадминов')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-sisadminov')[2])


@dp.message_handler(regexp= 'Про программистов')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-programmistov')[2])


@dp.message_handler(regexp= 'Старые и бородатые')
async def msg_handler(message: types.Message):
    await message.reply(get_text('starie-i-borodatie')[2])


@dp.message_handler(regexp= 'Про бухгалтеров')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-buhgalterov')[2])


@dp.message_handler(regexp= 'Про Била Гейтса')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-billa-geytsa')[2])


@dp.message_handler(regexp= 'Пошлые')
async def msg_handler(message: types.Message):
    await message.reply(get_text('poshlie-i-intimnie')[2])


@dp.message_handler(regexp= 'Про геншин')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-genshin')[2])


@dp.message_handler(regexp= 'Разные')
async def msg_handler(message: types.Message):
    await message.reply(get_text('raznie')[2])


@dp.message_handler(regexp= '️Про чукчей')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-chukchu')[2])


@dp.message_handler(regexp= 'Про вовочку')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-vovochku')[2])


@dp.message_handler(regexp= 'Про новых русских')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-novih-russkih')[2])


@dp.message_handler(regexp= 'Про шоу бизнес')
async def msg_handler(message: types.Message):
    await message.reply(get_text('po-shou-biznes')[2])


@dp.message_handler(regexp= 'Про алкоголиков')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-alkogolikov')[2])


@dp.message_handler(regexp= 'Про мужчин')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-mugchin')[2])


@dp.message_handler(regexp= 'Про детей')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-detey')[2])


@dp.message_handler(regexp= 'Про судей')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-sudey')[2])


@dp.message_handler(regexp= 'Народные')
async def msg_handler(message: types.Message):
    await message.reply(get_text('narodnie')[2])


@dp.message_handler(regexp= 'Советские')
async def msg_handler(message: types.Message):
    await message.reply(get_text('sovetskie')[2])


@dp.message_handler(regexp= 'Про Ржевского')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-poruchika-rgevskogo')[2])


@dp.message_handler(regexp= 'Про компьютеры')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-kompyuteri')[2])


@dp.message_handler(regexp= 'Про кино')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-kino')[2])


@dp.message_handler(regexp= 'Про животных')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-givotnih')[2])


@dp.message_handler(regexp= 'Политические')
async def msg_handler(message: types.Message):
    await message.reply(get_text('politicheskie')[2])


@dp.message_handler(regexp='X-files')
async def msg_handler(message: types.Message):
    await message.reply(get_text('pro-putina')[2])


@dp.message_handler(commands=['info'])
async def process_help_command(message: types.Message):
    await message.reply(info_message)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(help_message)


if __name__ == '__main__':
    money = threading.Thread(name="money", target=dollar.check_currency)
    money.start()
    executor.start_polling(dp)

