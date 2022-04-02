import requests
from bs4 import BeautifulSoup
import time
import smtplib


class Currency_DOLL:
    DOLLAR_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0\
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

    # Метод для получения курса валюты
    def get_currency_price(self):
        # Парсим всю страницу
        full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)

        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_page.content, 'html.parser')
        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        return convert[0].text  # .text метод BS4 который переводит tag -> str

    # Проверка изменения валюты
    def check_currency(self):
        currency = float(self.get_currency_price().replace(",", "."))
        if currency >= self.current_converted_price + self.difference:
            print("Курс сильно вырос, может пора что-то делать?")
            self.send_mail()
        elif currency <= self.current_converted_price - self.difference:
            print("Курс сильно упал, может пора что-то делать?")
            self.send_mail()

        print("Сейчас курс: 1 доллар = " + str(currency))
        time.sleep(3)  # Засыпание программы на 3 секунды
        self.check_currency()

        # Отправка почты через SMTP
        def send_mail(self):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login('ivaxen2000@gmail.com', 'local321')

            subject = 'ivaxen2000@gmail.com'
            body = f'Currency has been changed! {str(currency)}'
            message = f'Subject: {subject}\n{body}'

            server.sendmail(
                'От кого',
                'Кому',
                message
            )
            server.quit()


class Currency_EVRO:
    EVRO_RUB = 'https://www.google.com/search?q=%D0%B3%D1%83%D0%B3%D0%BB+%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1\
    %80%D0%BE&oq=%D0%B3%D1%83%D0%B3%D0%BB+%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&aqs=chrome..69i57j0i22\
    i30l4j0i22i30i457j0i22i30l4.6480j1j4&client=ubuntu&sourceid=chrome&ie=UTF-8'
    # Заголовки для передачи вместе с URL
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko)\
    Chrome/80.0.3987.149 Safari/537.36'}

    current_converted_price = 0
    difference = 5  # Разница после которой будет отправлено сообщение на почту

    def __init__(self):
        # Установка курса валюты при создании объекта
        self.current_converted_price = float(self.get_currency_price().replace(",", "."))

    # Метод для получения курса валюты
    def get_currency_price(self):
        # Парсим всю страницу
        full_page = requests.get(self.EVRO_RUB, headers=self.headers)

        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_page.content, 'html.parser')

        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        return convert[0].text  # .text метод BS4 который переводит tag -> str

    # Проверка изменения валюты
    def check_currency(self):
        currency = float(self.get_currency_price().replace(",", "."))
        if currency >= self.current_converted_price + self.difference:
            print("Курс сильно вырос, может пора что-то делать?")
            self.send_mail()
        elif currency <= self.current_converted_price - self.difference:
            print("Курс сильно упал, может пора что-то делать?")
            self.send_mail()

        print("Сейчас курс: 1 евро = " + str(currency))
        time.sleep(3)  # Засыпание программы на 3 секунды
        self.check_currency()

        # Отправка почты через SMTP
        def send_mail(self):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login('ivaxen2000@gmail.com', 'local321')

            subject = 'ivaxen2000@gmail.com'
            body = f'Currency has been changed! {str(currency)}'
            message = f'Subject: {subject}\n{body}'

            server.sendmail(
                'От кого',
                'Кому',
                message
            )
            server.quit()


# Создание объекта и вызов метода
currency_DOLL = Currency_DOLL()
# currency_DOLL.check_currency()
currency_EVRO = Currency_EVRO()
print(currency_DOLL.__dict__['current_converted_price'])
print(currency_EVRO.__dict__['current_converted_price'])
# currency_EVRO.check_currency()
# print(getattr(Currency_EVRO, "difference"))