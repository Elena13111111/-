# - Декоратор для замера времени выполнения функции
# замер времени любой функции

import time #импортируем время
import requests #для сайтов -запрос

def check_time(func): # функция принимает параметр func
    def inner(*args, **kwargs): #  тут 2 аргумента, кот.принимают
        start_time = time.time()    #начало времени
        res = func(*args, **kwargs) #вызов функции, кот. выполняет информацию
        finish_time = time.time()  #конец времени
        print(f'Функция выполнилась за {finish_time - start_time} секунд') #замер времени= конец - начало врермя.
        return res # возвращает результат

    return inner

@check_time #вызов декоратора -таймера
def f1():
    print('111111')
    time.sleep(2)
    print('222222')
# f1()
# >111111
# >222222
# >Функция выполнилась за 2.0004234313964844 секунд

@check_time
def fibonachi(num): #находим послее число Фибоначи, это ряд чисел, в котором каждое следующее число равно сумме двух предыдущих.
    if num in [1, 2]: # если наше число 1 или 2
        return num    # мы его возвращаем
    return fibonachi(num - 1) + fibonachi(num - 2)
# print(fibonachi(5))
# >>8
# for i in range (1, 5):
#     print(fibonachi(i))
# >  1
# >  2
# >  3
# > 5
# > 8

@check_time # запрос сайта
def f3():
    res = requests.get('https://www.google.by/') #запрос (сайт)
    res1 = requests.get('https://www.google.by/')
    res2 = requests.get('https://www.google.by/')
f3()




