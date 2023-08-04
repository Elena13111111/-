import sqlite3
from sqlite3 import Error
# pip install psycopg2
import psycopg2
from abc import ABC, abstractmethod
import pandas as pd


class DataClient(ABC):
    @abstractmethod
    def get_connection(self):
        pass

    @abstractmethod
    def create_mebel_table(self, conn):
        pass

# переписать с помощью pandas
    @abstractmethod
    def get_items(self, conn, price_from=0, price_to=100000):
        pass

    # переписать
    @abstractmethod
    def insert(self, conn, link, price, description):
        pass

    def run_test(self):
        conn = self.get_connection()
        self.create_mebel_table(conn)
        items = self.get_items(conn, price_from=10, price_to=30)
        for item in items:
            print(item)
        conn.close()


class PostgresClient(DataClient):
    USER = "postgres"
    PASSWORD = "postgres"
    HOST = "localhost"
    PORT = "5432"

    def get_connection(self):
        try:
            connection = psycopg2.connect(
                user=self.USER,
                password=self.PASSWORD,
                host=self.HOST,
                port=self.PORT
            )
            return connection
        except Error:
            print(Error)

    def create_mebel_table(self, conn):
        cursor_object = conn.cursor()
        cursor_object.execute(
            """
                CREATE TABLE IF NOT EXISTS mebel
                (
                    id serial PRIMARY KEY, 
                    link text, 
                    price integer, 
                    description text
                )
            """
        )
        conn.commit()

    # переписать с помощью pandas
    def get_items(self, conn, price_from=0, price_to=100000):
        query = f"select * from mebel where price >= {price_from} and price <= {price_to}"
        df = pd.read_sql_query(query, conn)
        return df
        # cursor = conn.cursor()
        # cursor.execute(f'SELECT * FROM mebel WHERE price >= {price_from} and price <= {price_to}')
        # return cursor.fetchall()

    # переписать
    def insert(self, conn, link, price, description):
        # query = (f"INSERT INTO mebel (link, price, description) VALUES ('{link}', '{price}', '{description}')")
        # values = (link, price, description)
        #
        # with self.conn.cursor() as cursor:
        #     cursor.execute(query, values)
        #     self.conn.commit()

        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO mebel (link, price, description) VALUES ('{link}', '{price}', '{description}')")
        conn.commit()


class Sqlite3Client(DataClient):
    DB_NAME = "kufar.db"

    def get_connection(self):
        try:
            conn = sqlite3.connect(self.DB_NAME)
            return conn
        except Error:
            print(Error)

    def create_mebel_table(self, conn):
        cursor_object = conn.cursor()
        cursor_object.execute(
            """
                CREATE TABLE IF NOT EXISTS mebel
                (
                    id integer PRIMARY KEY autoincrement, 
                    link text, 
                    price integer, 
                    description text
                )
            """
        )
        conn.commit()

    # переписать с помощью pandas
    def get_items(self, conn, price_from=0, price_to=100000):
        query = f"select * from mebel where price >= {price_from} and price <= {price_to}"
        df = pd.read_sql_query(query, conn)
        return df
     # pd.read_sql_query для выполнения SQL-запроса и создания объекта DataFrame из результата запроса.
     # Возвращается объект DataFrame с данными из таблицы "mebel" в указанном диапазоне цен.
        # cursor = conn.cursor()
        # cursor.execute(f'SELECT * FROM mebel WHERE price >= {price_from} and price <= {price_to}')
        # return cursor.fetchall()

    # переписать
    def insert(self, conn, link, price, description):
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO mebel (link, price, description) VALUES ('{link}', '{price}', '{description}')")
        conn.commit()
        # query = (f"INSERT INTO mebel (link, price, description) VALUES ('{link}', '{price}', '{description}')")
        # values = (link, price, description)
        #
        # with self.conn.cursor() as cursor:
        #     cursor.execute(query, values)
        #     self.conn.commit()
#Этот код использует контекстный менеджер with для установки автоматического закрытия курсора после его
# использования. Запрос SQL и значения параметров теперь передаются в метод execute курсора с использованием
# плейсхолдеров %s. Значения передаются в виде кортежа values. Затем выполняется команда commit для сохранения
# изменений в базе данных.

# data_client = PostgresClient()
data_client = Sqlite3Client()
data_client.run_test()
