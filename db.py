
import psycopg2
from psycopg2 import Error
from config import user_DB, password_DB

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
    cursor.execute("SELECT id, topic, content FROM anekdot WHERE id > 1000 and id < 1003; ")
    # Получить результат
    records = cursor.fetchone()
    print(len(records), type(records), records)
    # for record in records:
    #     print("topic =",  record[])

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")