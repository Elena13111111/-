# Занятие 5. Sqlite3
# - Парсим больше данных
# - Подключаемся к БД из Python
# - Концепкция Connection -> Cursor
# - Знакомство с sqlite3
# href - это ссылка, текст

#mebel.csv удаляем наш файл  слева.
import requests
from bs4 import BeautifulSoup
import pandas
import sqlite   #ссылка для наш файл

# файл для ссылок
links_to_parse = [
    'https://www.kufar.by/l/mebel',
    'https://www.kufar.by/l/mebel?cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6Mn0%3D',
    'https://www.kufar.by/l/mebel?cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6M30%3D',
    'https://www.kufar.by/l/mebel?cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6NH0%3D'
]

# по одной ссылке /странице
def get_mebel_by_link(link):  #link - это ссылка по кот.хотим получить мебель
    response = requests.get(link)
    mebel_data = response.text

    mebel_items = []
    to_parse = BeautifulSoup(mebel_data, 'html.parser')
    for elem in to_parse.find_all('a', class_='styles_wrapper__5FoK7'):
        try:
            price, decription = elem.text.split('р.')   # цена и описание = разделение   /Дебаг >>price.replace(' ', '')
            mebel_items.append((
                elem['href'],                 # 1-ое ссылка
                int(price.replace(' ', '')),  # 2-ое цена -  эту строку заменяем на число (было 1 270 >> стало 1270)
                decription                    # 3-е текст
            ))
        except:
            print(f'Цена не была указана. {elem.text}')  #для проверки , что было написано вставляем елемент
        # mebel_items.append((elem['href'], elem.text))  # тут Дебаг.пишем elem.text - и нам показывает ЦЕНУ и текст все вместе
        # #тут Дебаг.пишем : elem.text.split('р.') --> разделает строки ЦЕну и название

    return mebel_items

 #сохранение в sqlite
def save_to_sqlite(mebel_items):
    connection = sqlite.get_connection()   #ссылка файла = соединение
    for item in mebel_items:   #элемент из списка
        sqlite.insert(connection, item[0], item[1], item[2])   #обращение на ссылку файла и на фукцию


def save_to_csv(mebel_items):  # сохранение
    pandas.DataFrame(mebel_items).to_csv('mebel.csv', index=False)

#проходим по циклу
def run(): # запуск
    mebel_items = []    # пустой список
    for link in links_to_parse:  # из наших ссылок (сверху)
        mebel_items.extend(get_mebel_by_link(link))  # в этот список будем добавлять новый список
    save_to_sqlite(mebel_items)  #сохраняем (слева) в csv


run()
# # >> слева появляеться файл с нашими : 0, 1, 2 : ссылка, цена, описание
# >> Цена не была указана. ДоговорнаяИзготавливаем шкафы на заказ любой сложности.Брест
