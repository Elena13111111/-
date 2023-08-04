# Занятие 4. Парсим красиво
# - Парсим отдельные объекты с куфара
# - Сохраняем их в .csv и знакомимся с pandas
#bs4 -> для Парсинг /beautifulsoup
# заходим на сайт www.kufar.by, выбираем мебель, кликаем на страницу правой кнопки мыши -->Исследовать элемент.
#открывается код страницы. Сегодня ищем общие черты

# import requests
# from bs4 import BeautifulSoup
# import pandas
#
# # pip install beautifulsoup4    -->импортируем
# # pip install pandas
#
# response = requests.get('https://www.kufar.by/l/mebel')   # requests --> благодаря этому мы получаем html страницы
# mebel_data = response.text    # mebel_data --> это результат запроса
#
# to_parse = BeautifulSoup(mebel_data, 'html.parser')
# # for elem in to_parse.find_all('a', class_='styles_wrapper__yaLfq'):
# for elem in to_parse.find_all('a', class_='styles_wrapper__5FoK7'):   #выбираем секции (section)
#     #find_all --> найти в страничке, 'div' --> тип блока кот.ищем
#     print(f'-{elem}')
# вывод : на экране показывает код страницы и ссылки
# >>-<a class="styles_wrapper__5FoK7" href="https://www.kufar.by/item/101518142?searchId=3e1d41f483db3bbdf095e99f599619cfcf5c" target="_blank"><div class="styles_image__kwQfE"><
# -----------------------------
# Парсим один элемент / одну страницу
# import requests
# from bs4 import BeautifulSoup
# import pandas
#
# response = requests.get('https://www.kufar.by/l/mebel')
# mebel_data = response.text
#
# mebel_items = {}
# to_parse = BeautifulSoup(mebel_data, 'html.parser')
# for elem in to_parse.find_all('a', class_='styles_wrapper__yaLfq'):
#     mebel_items = [elem['href']] = elem.text
#
# print()
# debug на Принт, выбираем mebel_items  --> показывает ссылки



# _________________________________

import requests
from bs4 import BeautifulSoup
import pandas

def get_mebel_items(link):  #link - это ссылка по кот.хотим получить мебель
    response = requests.get(link)
    mebel_data = response.text

    mebel_items = []
    to_parse = BeautifulSoup(mebel_data, 'html.parser')
    for elem in to_parse.find_all('a', class_='styles_wrapper__5FoK7'):
        mebel_items.append((elem['href'], elem.text))  #href - это ссылка, текст

    return mebel_items


def save_to_csv(mebel_items):  # сохранение
    pandas.DataFrame(mebel_items).to_csv('mebel.csv', index=False)


def run():
    mebel_items = get_mebel_items('https://www.kufar.by/l/mebel')
    save_to_csv(mebel_items)   # тут Дебаг, вводим mebel_items и нам выдает ссылки на страничку


run()
# >> слева появляеться файл с нашими ссылками и текст