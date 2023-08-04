# Занятие 24. Полиморфизм
# - Полиморфизм -  один интерфейс и множество реализаций
# - Интерфейсы/Абстрактные классы
# - Циклом пройтись по списку интерфейсов
# - NotImpementedError
# - abc

# Полиморфизм- это множество форм. Что-то одно, кот.может явл-ся чем-то разным.
# Без наследования Полиморфизм не может быть. Полиморфизм Это возможность вызывать
# какой-то кол-во объектов под общим интерфейсом. Он реализуеться на базе наследования
# Сигнатуры функции- это имя функции func и кол-во его параметров и типы параметров (number, name). Сигнатуры уникальна.

#это не Полиморфизм
# def func(number, name):  # Сигнатура
#     print(number, name)
#
# def func(number, name, name2):
#     print(number, name, name2)
#
# func(123, 'ffff')
# func(123, 'ffff', 'mmmm')
# >> Error
#
# ФУнкция с именем может быть только одна (func).
# ----------------------------------
# class Printable:
#     def pretty_print(self):
#         print(f'======={self}=======')
#
# class Car(Printable):
#     def drive(self):
#         print('Машина едет')
#
# class Dog(Printable):
#     def gav(self):
#         print('Собака лает')
#
# car = Car()
# dog = Dog()
#
# # car.drive() # вызов класса со своими методами
# # dog.gav()
# # >>Машина едет
# # >>Собака лает
#
# printables = [car, dog] # берем объект и ложим все в список (делаем ссылку на род.класс)
# for obj in printables:  # для каждого объекта из printables
#     obj.pretty_print()  #  вызываем функцию pretty_print
# # >=======<__main__.Car object at 0x000001CDE90CEE50>=======
# # =======<__main__.Dog object at 0x000001CDE90CF790>=======
# ====================================

# class Printable:
#     def pretty_print(self):
#         raise NotImplemented ('ФУнкция должна быть реализована') #исключение
#
# class Car(Printable):
#     def drive(self):
#      print('Машина едет')
#     def pretty_print(self):
#         print('Красивая машина ')
#
# class Dog(Printable):
#     def pretty_print(self):
#         print('Красивая собака ')
#     def gav(self):
#         print('Собака лает')
#
# class Cat(Printable):
#     def miay(self):
#         print('Кошка мяукает')
#
# car = Car()
# dog = Dog()
# cat = Cat()
#
# #
# # printables = [car, dog] # берем объект и ложим все в список (делаем ссылку на род.класс)
# # for obj in printables:  # для каждого объекта из printables
# #     obj.pretty_print()   #вызываем этот интерфейс
# #>> Красивая машина
# #>> Красивая собака
#
# printables = [car, dog, cat] # берем объект и ложим все в список (делаем ссылку на род.класс)
# for obj in printables:  # для каждого объекта из printables
#     obj.pretty_print()   #вызываем этот интерфейс
# >> Error
# У класса Cat нет функции obj.pretty_print(), потому просиходит ошибка.
# --------------------------------
# правильное выполнение (красиво) верхнего примера. Полиморфизм
# нужен abc импортируем для абстрактных методов
# from abc import  ABC,abstractmethod
#
# class Printable(ABC):
#     @abstractmethod  #абстрактный методов
#     def pretty_print(self):
#         pass
#
# class Car(Printable):
#     def pretty_print(self):
#         print('Красивая машина ')
#
# class Dog(Printable):
#     def pretty_print(self):
#         print('Красивая собака ')
#
#
# class Cat(Printable):
#     def pretty_print(self):
#         print('Кошка мяукает')
#
# car = Car()
# dog = Dog()
# cat = Cat()
# #
#
# printables = [car, dog, cat] # берем объект и ложим все в список (делаем ссылку на род.класс)
# for obj in printables:  # для каждого объекта из printables
#     obj.pretty_print()   #вызываем этот интерфейс
# # >>Красивая машина
# # Красивая собака
# # Кошка мяукает
# ============================================
# from abc import  ABC,abstractmethod
#
# class Printable(ABC):
#     @abstractmethod  #абстрактный методов
#     def pretty_print(self):
#         pass
# # Полиморфизм Это возможность вызывать какой-то кол-во объектов под общим интерфейсом. Он реализуеться на базе наследования
#     def final_print(self):  #базовый метод, кот. включает абстрактный метод
#         print('=' * 30)
#         self.pretty_print()
#         print('=' * 30)
#
#
# class Car(Printable):
#     def pretty_print(self):
#         print( 'Красивая машина ')
#
# class Dog(Printable):
#     def pretty_print(self):
#         print( 'Красивая собака ')
#
#
# class Cat(Printable):
#     def pretty_print(self):
#         print( 'Кошка мяукает')
#
# car = Car()
# dog = Dog()
# cat = Cat()
# printables = [car, dog, cat] # берем объект и ложим все в список (делаем ссылку на род.класс)
# for obj in printables:  # для каждого объекта из printables
#     obj.final_print()
# >>==============================
# Красивая машина
# ==============================
# ==============================
# Красивая собака
# ==============================
# ==============================
# Кошка мяукает
# ==============================

# ---------------------------------
from abc import ABC, abstractmethod

class BirthDay(ABC):
    @abstractmethod
    def get_name(self):
        pass

    def congritulate(self):
        # ...
        print(f'Поздравляем тебя {self.get_name()} с днём рождения')
        # ...
        # ...
        # ...

class Car(BirthDay):
    def get_name(self):
        return 'Машина'


class Dog(BirthDay):
    def get_name(self):
        return 'Шарик'


class Cat(BirthDay):
    def get_name(self):
        return 'Шурик'

car = Car()
dog = Dog()
cat = Cat()
printables = [car, dog, cat]
for obj in printables:
    obj.congritulate()

# >Поздравляем тебя Машина с днём рождения
# Поздравляем тебя Шарик с днём рождения
# Поздравляем тебя Шурик с днём рождения


