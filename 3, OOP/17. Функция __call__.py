# Занятие 17. Функция __call__
# __call__
# Замыкания
# Декораторы

# Все магические методы с двумя подчеркиванием (__).
1. Магический метод __call__. это аналог замыкания
Замыкание- это две функции собранные, кот.:
1. сущ-ует для хранения каких-то данных на постоянке.
2. для реализации логики.

class Dog():
    def __init__(self):
        print('Гав-гав')

    def __call__(self, *args, **kwargs):
        print('Тяф-тяф')

dog = Dog()
dog() #этот метод __call__ вызываеться , при условияя что сначала вызываеться __init__
dog()
dog()
dog()

>>Гав-гав
Тяф-тяф
Тяф-тяф
Тяф-тяф
Тяф-тяф
# ========================
# Замыкания
class Counter():
    def __init__(self):
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.count

counter = Counter()
counter2 = Counter()
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())

print(counter2())
print(counter2())
print(counter2())

1
2
3
4
5
6
7

1
2
3
# =====================
# Декоратор на объекте класса
import time

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        res = self.func(*args, **kwargs)
        finish_time = time.time()
        print(f'Задание выполнено за :{finish_time - start_time} секунд')
        return res

@Timer
def do_any_action():
    print('1')
    time.sleep(0.5)
    print('2')
    time.sleep(0.5)
    print('3')
    time.sleep(0.5)
    print('4')


do_any_action()

>1
2
3
4
Задание выполнено за :1.5021030902862549 секунд




