import random
import psycopg2
from psycopg2 import Error
from config import user_DB, password_DB, list_of_text_in_base

host = "127.0.0.1"
port = 5432


def get_text(key_dict):
    """Функция для генерации случайного ID в нужном диапазоне и отправления запросов в БД и получения данных с базы"""
    id_send = random.randint(list_of_text_in_base[key_dict][0], list_of_text_in_base[key_dict][1])
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user=user_DB,
                                      password=password_DB,
                                      host=host,
                                      port=port,
                                      database="anekdot_db")
        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        # Выполнение SQL-запроса
        cursor.execute(f"SELECT id, topic, content FROM anekdot WHERE id = '{id_send}'; ")
        # Получить результат
        records = cursor.fetchone()
        return records

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


def send_currency_DOLL(dol):
    """Функция для отправки курса Доллара"""
    try:
        connection = psycopg2.connect(user=user_DB,
                                      password=password_DB,
                                      host=host,
                                      port=port,
                                      database="money_db")
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO dollar (type_of_currency, currency)"
                       f" VALUES ('USD', {dol}); ")
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


def send_currency_EVRO(evr):
    """Функция для отправки курса Евро"""
    try:
        connection = psycopg2.connect(user=user_DB, password=password_DB, host=host, port=port, database="money_db")
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO evro (type_of_currency, currency)"
                       f" VALUES ('EUR', {evr}); ")
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


def send_currency_BTC(btc):
    """Функция для отправки курса Биткоина"""
    try:
        connection = psycopg2.connect(user=user_DB, password=password_DB, host=host, port=port, database="money_db")
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO bitcoin (type_of_currency, currency)"
                       f" VALUES ('BTC', {btc}); ")
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
