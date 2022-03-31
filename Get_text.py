import random
import psycopg2
from psycopg2 import Error
from config import user_DB, password_DB, list_of_text_in_base


def get_text(key_dict):
    """Функция для генерации случайного ID в нужном диапазоне и отправления запросов в БД и получения данных с базы"""
    id_send = random.randint(list_of_text_in_base[key_dict][0], list_of_text_in_base[key_dict][1])
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user=user_DB,
                                      password=password_DB,
                                      host="127.0.0.1",
                                      port="5432",
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

