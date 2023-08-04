# Занятие 29. Множественное наследование
# - Множественное наследование. Порядок обхода, параметры
# - __mro__ (method resolution order)
# - Одинаковые имена методов


# from dataclasses import dataclass
#
# @dataclass(frozen=True)
# class Car():
#         model : str
#         year : int
#
# @dataclass(frozen=True)
# class Student():
#         name : str
#         last_name : str
#
# print(Car('джип m-204', 2022))
# print(Student('Иван', 'Кошкин'))
# >>Car(model='джип m-204', year=2022)
# >>Student(name='Иван', last_name='Кошкин')

# --------------------------------
#множ-ное наследование /сохранение в базу данных

# from dataclasses import dataclass
#
# #сохранение в базу данных
# class dbSaver:
#     def saver_to_db(self):
#        print(f'Сохранненo в базу данных : {self}')
#
#
# @dataclass(frozen=True)
# class Car(dbSaver):   #наследует от родителя
#         model : str
#         year : int
#
# @dataclass(frozen=True)
# class Student(dbSaver):    #наследует от родителя
#         name : str
#         last_name : str
#
# car= Car ('джип m-204', 2022)
# student = Student('Иван', 'Кошкин')
# to_save_elems = [car,student ]
# # проходим цикл
# for elem in to_save_elems:
#     elem.saver_to_db()    #вызов метода
# >>Сохранненo в базу данных : Car(model='джип m-204', year=2022)
# Сохранненo в базу данных : Student(name='Иван', last_name='Кошкин')

# --------------------------------------------------
#сохранение в базу данных и в екселе
#
# from dataclasses import dataclass
#
#
# class XLSXSaver:
#     def saver_to_excel(self):
#        print(f'Сохранненo в Excel : {self}')
#
# # #сохранение в базу данных
# class dbSaver:
#     def saver_to_db(self):
#        print(f'Сохранненo в базу данных : {self}')
#
# @dataclass(frozen=True)
# class Car(dbSaver, XLSXSaver):   #наследует от 2 родителя
#         model : str
#         year : int
#
# @dataclass(frozen=True)
# class Student(dbSaver, XLSXSaver):    #наследует от 2 родителя
#         name : str
#         last_name : str
#
# car= Car ('джип m-204', 2022)
# student = Student('Иван', 'Кошкин')
# to_save_elems = [car,student ]
# # проходим цикл
# for elem in to_save_elems:
#     elem.saver_to_db()
#     elem.saver_to_excel()
# >>Сохранненo в базу данных : Car(model='джип m-204', year=2022)
# Сохранненo в Excel : Car(model='джип m-204', year=2022)
# Сохранненo в базу данных : Student(name='Иван', last_name='Кошкин')
# Сохранненo в Excel : Student(name='Иван', last_name='Кошкин')

# ------------------------------------------------------

# - __mro__ (method resolution order) /Порядок вызова метода

# from dataclasses import dataclass
#
# class XLSXSaver:
#     def saver_to_excel(self):
#        print(f'Сохранненo в Excel : {self}')
#
# # #сохранение в базу данных
# class dbSaver:
#     def saver_to_db(self):
#        print(f'Сохранненo в базу данных : {self}')
#
# @dataclass(frozen=True)
# class Car(dbSaver, XLSXSaver):   #наследует от 2 родителя
#         model : str
#         year : int
#
# @dataclass(frozen=True)
# class Student(dbSaver, XLSXSaver):    #наследует от 2 родителя
#         name : str
#         last_name : str
#
# car= Car ('джип m-204', 2022)
# student = Student('Иван', 'Кошкин')
# to_save_elems = [car,student ]
# # проходим цикл
# # for elem in to_save_elems:
# #     elem.saver_to_db()
# #     elem.saver_to_excel()
#
# print(Car.__mro__)
# print(Student.__mro__)
#нам показывает порядок наследование/иерархия
# >>(<class '__main__.Car'>, <class '__main__.dbSaver'>, <class '__main__.XLSXSaver'>, <class 'object'>)
# (<class '__main__.Student'>, <class '__main__.dbSaver'>, <class '__main__.XLSXSaver'>, <class 'object'>)

# -----------------------
from dataclasses import dataclass

# class XLSXSaver:
#     def __init__(self, arg1):  #добавляем аргу4ент
#         self.arg1 = arg1
#     def saver_to_excel(self):
#        print(f'Сохранненo в Excel : {self}')
#
# # #сохранение в базу данных
# class dbSaver:
#     def __init__(self, arg1):  #добавляем аргумент/ но не доб-яем в строку
#         self.arg1 = arg1
#     def saver_to_db(self):
#        print(f'Сохранненo в базу данных : {self}')
#
# class Car(dbSaver, XLSXSaver):   #наследует от 2 родителя
#     def __init__(self, model,year):
#         self.model =model
#         self.year = year
#
#     def __repr__(self):    #переопределение
#         return f'{self.model} {self.year}'
#
# class Student(dbSaver, XLSXSaver):    #наследует от 2 родителя
#     def __init__(self, name,last_name):
#         self.name = name
#         self.last_name = last_name
#
#     def __repr__(self):   #переопределение
#         return f'{self.name} {self.last_name}'
#
#
# car= Car ('джип m-204', 2022)
# student = Student('Иван', 'Кошкин')
# to_save_elems = [car,student ]
# # проходим цикл
# for elem in to_save_elems:
#     elem.saver_to_db()
#     elem.saver_to_excel()

# >>Сохранненo в базу данных : джип m-204 2022
# Сохранненo в Excel : джип m-204 2022
# Сохранненo в базу данных : Иван Кошкин
# Сохранненo в Excel : Иван Кошкин
# --------------------------------------

# добавляем аргумент

# основной
# class MainSaver:
#     def __init__(self, login, password):
#        self.login=login
#        self.password = password
#
#     def main_save(self):
#         print(f'[{self.login} - {self.password}] Основное сохранение {self}')
# class XLSXSaver:
#     def __init__(self, arg1):  #добавляем аргумент
#         # self.arg1 = arg1
#         pass
#     def saver_to_excel(self):
#        print(f'{self}Сохранненo в Excel : {self}')
#
# # #сохранение в базу данных
# class dbSaver:
#     def __init__(self):  #добавляем аргумент
#         pass
#     def saver_to_db(self):
#        print(f'Сохранненo в базу данных : {self}')

#MainSaver - это основной класс Родителя
# dbSaver, XLSXSaver - это Миксины / дополнительный класс/ они без параметров (Инит пустые)
# class Car(MainSaver,dbSaver, XLSXSaver):   #наследует от 2 родителя
#     def __init__(self, model,year):
#         super().__init__('login1', 'password1')     #нужно для передачи аргумента
#         self.model =model
#         self.year = year
#
#     def __repr__(self):    #переопределение
#         return f'{self.model} {self.year}'
#
# class Student(MainSaver,dbSaver, XLSXSaver):    #наследует от 2 родителя
#     def __init__(self, name,last_name):
#         super().__init__('login2', 'password2')  # нужно для передачи аргумента
#         self.name = name
#         self.last_name = last_name
#
#     def __repr__(self):   #переопределение
#         return f'{self.name} {self.last_name}'
#
# car= Car ('джип m-204', 2022)
# student = Student('Иван', 'Кошкин')
# to_save_elems = [car,student ]
# # проходим цикл
# for elem in to_save_elems:
#     elem.main_save()
#     elem.saver_to_db()
#     elem.saver_to_excel()

#>> [login1 - password1] Основное сохранение джип m-204 2022
# Сохранненo в базу данных : джип m-204 2022
# джип m-204 2022Сохранненo в Excel : джип m-204 2022
# [login2 - password2] Основное сохранение Иван Кошкин
# Сохранненo в базу данных : Иван Кошкин
# Иван КошкинСохранненo в Excel : Иван Кошкин

# _____________________________________
#
from dataclasses import dataclass


class MainSaver:
    def __init__(self):
        print('MainSaver.__init__')
        super().__init__()

    def main_save(self):
        print(f'MainSaver {self}')



class XLSXSaver:
    def __init__(self):
        print('XLSXSaver.__init__')
        super().__init__()
        super().__init__()
    def save_to_excel(self):
        print(f'Сохранено в EXCEL: {self}')

    def main_save(self):
        print(f'XLSXSaver {self}')


class DbSaver:
    def __init__(self):
        print('DbSaver.__init__')
        super().__init__()

    def main_save(self):
        print(f'DbSaver {self}')

#если у нас на 1-ом месте стоит DbSaver, значит этот параметр вызывается первым
class Car(DbSaver, MainSaver, XLSXSaver):
    def __init__(self, model, year):
        print('Car.__init__')
        super().__init__()  # чтобы вызвать XLSXSaver  и DbSaver
        self.model = model
        self.year = year

    def __repr__(self):
        return f'{self.model} {self.year}'


class Student(MainSaver, DbSaver, XLSXSaver):
    def __init__(self, name, last_name):
        print('Student.__init__')
        super().__init__()  # чтобы вызвать XLSXSaver и DbSaver
        self.name = name
        self.last_name = last_name

    def __repr__(self):
        return f'{self.name} {self.last_name}'


car = Car('Ферари SF 900', 2018)
student = Student('Петров', 'Иван')
to_save_elems = [car, student]

print('=' * 60)
for elem in to_save_elems:
    elem.main_save()

# >>Car.__init__
# DbSaver.__init__
# MainSaver.__init__
# XLSXSaver.__init__
# Student.__init__
# MainSaver.__init__
# DbSaver.__init__
# XLSXSaver.__init__
# ==============================
# DbSaver Ферари SF 900 2018
# MainSaver Петров Иван



