import sqlite3
from sqlite3 import Error


# создали соединение
def get_connection(): #connection это канал(соединение), через кот. мы можем что-то делать с Базой Данных
    try:
        conn = sqlite3.connect('kufar.db')   # база данных сайта куфар
        return conn
    except Error:           # проверка на ошибки Error
        print(Error)

        # таблица              # порядок действия
        # 0. connection
        # 1.cursor- отвечает за конкретный запрос
        # 2. execute
        # 3. commit
        # CREATE TABLE IF NOT EXISTS mebel  # название Таблицы Мебель
        # (
        #     id integer PRIMARY KEY autoincrement,  # ид ключ
        #     link text,  # ссылка
        #     price integer,  # цена
        #     description text  # описание
        # )
def create_mebel_table(conn):     # 0. connection
    cursor_object = conn.cursor()  # 1.cursor- отвечает за конкретный запрос
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

 #python sqlite select/
def get_items(conn, price_from=0, price_to=100000):    # соединение, цена от, цена до
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM mebel WHERE price >= {price_from} and price <= {price_to}')
    # выбираем Всё мебель где цена больше/равно цена_от и цена меньше/равно Цена_до
    return cursor.fetchall()    # вернуть и забрать данные

 #python sqlite insert/ сохранение выполнение команд
def insert(conn, link, price, description):      #принимает  соединение, цена, описание
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO mebel (link, price, description) VALUES ('{link}', '{price}', '{description}')")
    conn.commit()     # для сохранения соединеия

 #проверка
def sqlite_test():
    conn = get_connection()
    create_mebel_table(conn)
    items = get_items(conn, 10, 200)  #цена  от 10 до 200
    for item in items:
        print(item)
    conn.close()   # закрыть соединение


sqlite_test()
#
# >>(9, 'https://www.kufar.by/item/177227223?rank=7&searchId=db686e5d0529725fcb4562156c80ddc75ae6', 123, 'Банкетка новая 60смГродноДоставка по Беларуси')
# (10, 'https://www.kufar.by/item/202556021?rank=8&searchId=db686e5d0529725fcb4562156c80ddc75ae6', 12, 'Вешалки икея Брест')
# (11, 'https://www.kufar.by/item/202555859?rank=9&searchId=db686e5d0529725fcb4562156c80ddc75ae6', 15, 'Журнальный столВитебск')
# (12, 'https://www.kufar.by/item/202555854?rank=10&searchId=db686e5d0529725fcb4562156c80ddc75ae6', 50, 'Стол и стул ПолесьеМогилевская, Бобруйск')
# (13, 'https://www.kufar.by/item/202555855?rank=11&searchId=db686e5d0529725fcb4562156c80ddc75ae6', 30, 'Стул компьютерный Гродно')
# (16, 'https://www.kufar.by/item/202555800?rank=14&searchId=db686e5d0529725fcb4562156c80ddc75ae6', 70, 'Створки шкафа-купеМогилев')