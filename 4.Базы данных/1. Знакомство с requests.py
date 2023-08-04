# Занятие 1. Знакомство с requests
# Знакомство с requests


# requests - это запрос
# он позволяет ходить по интернету и получать данные по url
# requests - Позволяет отправлять запросы и брать данные где-то из интернета
# -------------------------------

# pip install requests  --> загружаем в Терминал


import requests   #импортируем
import json     # достаем данные

response = requests.get('https://api.sampleapis.com/coffee/hot')
coffe_data = json.loads(response.text)  #возвращает html страницы

for num, data in enumerate(coffe_data):
    print(f'{num}. {coffe_data}')



# ===================================
# import requests
#
# res = requests.get('https://api.sampleapis.com/coffee/hot')
#
# print()


#дебаг на Принт -- пишем res.text

# -----------------------------
# import requests
#
# res = requests.get('https://api.sampleapis.com/coffee/hot')
#
# print()

#дебаг на Принт -- пишем json.loads(res.text)