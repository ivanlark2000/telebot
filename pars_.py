import asyncio
import requests
import time
import threading
from aiogram import Bot
from bs4 import BeautifulSoup
from Get_text import send_currency_DOLL, send_currency_EVRO, send_currency_BTC
from config import TOKEN

bot = Bot(TOKEN)
CHANNEL_ID = '@helloword2000'


class Currency_DOLL:
    current_site = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0\
    +%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&client=ubuntu&sxsrf=APq-WBvgikTUBWbEP4EOZ4dNNy1uZ6iFdA%3A1648835026764&ei\
    =0jlHYoaSLoT5rgSg96HICw&oq=%D0%B3%D1%83%D0%B3%D0%BB+%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80\
    %D0%B0&gs_lcp=Cgdnd3Mtd2l6EAEYADIHCAAQRxCwAzIHCAAQRxCwAzIKCAAQRxCwAxDJAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQR\
    xC\wAzIHCAAQRxCwAzIHCAAQsAMQQ0oECEEYAEoECEYYAFAAWABg2oMbaAFwAXgAgAEAiAEAkgEAmAEAyAEJwAEB&sclient=gws-wiz'
    # Заголовки для передачи вместе с URL
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko)\
    Chrome/80.0.3987.149 Safari/537.36'}
    current_converted_price = 0
    difference = 5  # Разница после которой будет отправлено сообщение на почту

    def __init__(self):
        # Установка курса валюты при создании объекта
        self.current_converted_price = float(self.get_currency_price().replace(",", "."))

    def get_currency_price(self):
        # Парсим всю страницу
        full_page = requests.get(self.current_site, headers=self.headers)
        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_page.content, 'html.parser')
        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        return convert[0].text  # .text метод BS4 который переводит tag -> str

    # Проверка изменения валюты
    def check_currency(self):
        currency = float(self.get_currency_price().replace(",", "."))
        if currency >= self.current_converted_price + self.difference:
            asyncio.run(send_currency(f"Курс доллара вырос, был {self.current_converted_price - self.difference} руб "
                                      f"стал {currency} руб. может пора что-то делать?"))
        elif currency <= self.current_converted_price - self.difference:
            asyncio.run(send_currency(f"Курс доллара упал, был {self.current_converted_price - self.difference} руб "
                                      f"стал {currency} руб. может пора что-то делать?"))
        print("Сейчас курс: 1 доллар = " + str(currency) + ' руб')
        time.sleep(120)  # Засыпание программы на 5 секунды
        send_currency_DOLL(currency)
        self.check_currency()


class Currency_EVRO(Currency_DOLL):
    current_site = 'https://www.google.com/search?q=%D0%B3%D1%83%D0%B3%D0%BB+%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1\
    %80%D0%BE&oq=%D0%B3%D1%83%D0%B3%D0%BB+%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&aqs=chrome..69i57j0i22\
    i30l4j0i22i30i457j0i22i30l4.6480j1j4&client=ubuntu&sourceid=chrome&ie=UTF-8'

    def check_currency(self):
        currency = float(self.get_currency_price().replace(",", "."))
        if currency >= self.current_converted_price + self.difference:
            asyncio.run(send_currency(f"Курс евро вырос, был {self.current_converted_price - self.difference} руб "
                                      f"стал {currency} руб. может пора что-то делать?"))
        elif currency <= self.current_converted_price - self.difference:
            asyncio.run(send_currency(f"Курс евро упал, был {self.current_converted_price - self.difference} руб "
                                      f"стал {currency} руб. может пора что-то делать?"))

        print("Сейчас курс: 1 евро = " + str(currency) + ' руб')
        time.sleep(180)  # Засыпание программы на 5 секунды
        send_currency_EVRO(currency)
        self.check_currency()


class Currency_BTC(Currency_DOLL):
    current_site = 'https://www.google.com/finance/quote/BTC-RUB'
    difference = 10000

    def get_currency_price(self):
        # Парсим всю страницу
        full_page = requests.get(self.current_site, headers=self.headers)
        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_page.content, "html.parser")
        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("div", class_="YMlKec fxKbKc")
        return convert[0].text.replace(',', '')  # .text метод BS4 который переводит tag -> str

    def check_currency(self):
        currency = float(self.get_currency_price().replace(",", "."))
        if currency >= self.current_converted_price + self.difference:
            asyncio.run(send_currency(f"Курс BITCOIN сильно вырос, на {self.difference} руб. "
                                      f"был {self.current_converted_price - self.difference} "
                                      f"руб стал {currency} руб.  может пора что-то делать?"))
        elif currency <= self.current_converted_price - self.difference:
            asyncio.run(send_currency(f"Курс BITCOIN сильно упал, на {self.difference} руб."
                                      f"был {self.current_converted_price - self.difference} "
                                      f"руб. стал {currency} руб. может пора что-то делать?"))
        print("Сейчас курс: 1 BITCOIN = " + str(currency) + " руб")
        time.sleep(240)  # Засыпание программы на 5 секунды
        send_currency_BTC(currency)
        self.check_currency()


async def send_message(channel_id: int, text: str):
    await bot.send_message(channel_id, text)


async def send_currency(text):
    await send_message(CHANNEL_ID, text)

dollar = Currency_DOLL()
evro = Currency_EVRO()
btc = Currency_BTC()
if __name__ == "__main__":
    d = threading.Thread(name='doll', target=dollar.check_currency)
    e = threading.Thread(name='evro', target=evro.check_currency)
    b = threading.Thread(name='btc', target=btc.check_currency)
    d.start()
    e.start()
    b.start()
