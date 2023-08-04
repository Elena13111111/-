# Занятие 16. Дескрипторы
# - Дескриптор. Как убрать функциональное дублирование гетторов/сеттеров
# - data, non-data Дескрипторы

# сокращенный вариант
# Этот дексприптор. исп-ся этот класс для каждого из нашего координат. Этот класс для валидации атрибутов.
#Дескрипторы data -позволяет нам получать и читать данные.
#Дескрипторы non-data -позволяет нам только читать.
# 3 сокращенное
class IntegerCoordinate: # Этот дексприптор.
    @staticmethod
    def validate_point(num):
        return num if type(num) == int else 0
    # возвращаем Число равное Числовому значению, иначе 0

    # э то 3метода кот. всегда присутствуют.owner не трогаем

    def __set_name__(self, owner, name): #  имя переменных
        self.name = '_____' + name  #новое имя, кот. мы задаем

    def __get__(self, instance, owner):  # геттер.
        return getattr(instance, self.name) #instance - объект

    def __set__(self, instance, value):  # сеттер
        setattr(instance, self.name, self.validate_point(value)) # проверка на число

class Point:
    x = IntegerCoordinate()
    y = IntegerCoordinate()
    z = IntegerCoordinate()

    def __init__(self, x, y, z): # передаем координаты
        self.x = x
        self.y = y
        self.z = z

# point = Point(4, 10, 899)
# print(point.__dict__)
point1 = Point(1, 2, 'ndrthdt')
point2 = Point(100, 50, -20)
print(point1.__dict__)
print(point2.__dict__)
# >{'_____x': 1, '_____y': 2, '_____z': 0}
# >{'_____x': 100, '_____y': 50, '_____z': -20}
print(point2.x)
point2.x = 88 # меням число на другое
print(point2.x)
print(point2.__dict__)
>100
>88
>{'_____x': 88, '_____y': 50, '_____z': -20}

# __________________________________
#1
# полноценный вариант примера
# class Point:
#     def __init__(self, x, y, z): # передаем координаты / сеттер
#         self.set_x (self.validate_point(x))
#         self.set_y (self.validate_point(y))
#         self.set_z (self.validate_point(z))
#
#     def set_x(self, x):    #сеттер
#         self._x =self.validate_point(x)
#
#     def set_y(self, y):    #сеттер
#         self._y =self.validate_point(y)
#
#     def set_z(self, z):    #сеттер
#             self._z = self.validate_point(z)
#
#     def get_x(self):
#         return self._x
#
#     def get_y(self):
#         return self._y
#
##    def get_z(self):
#         return self._z
#
#     @staticmethod
#     def validate_point(num):
#         return num if type(num) == int else 0
#     # возвращаем Число равное Числовому значению, иначе 0
#
# point = Point (-68, 258, 45)
# print(point.__dict__, point.get_y())
# >>{'_x': -68, '_y': 258, '_z': 45} 258
# ________________________________________________
#2
# class IntegerCoordinate: # Этот дексприптор.
#     @staticmethod
#     def validate_point(num):
#         return num if type(num) == int else 0
#     # возвращаем Число равное Числовому значению, иначе 0
#
#     def __set_name__(self, owner, name):
#         pass
#
#     def __getattr__(self, item):  #геттер
#         pass
#
#     def __setattr__(self, key, value): # сеттер
#         pass
#
#
# class Point:
#     def __init__(self, x, y, z): # передаем координаты / сеттер
#          self.set_x (self.validate_point(x))
#          self.set_y (self.validate_point(y))
#          self.set_z (self.validate_point(z))
#
#     def set_x(self, x):    #сеттер
#             self._x =self.validate_point(x)
#
#     def set_y(self, y):    #сеттер
#             self._y =self.validate_point(y)
#
#     def set_z(self, z):    #сеттер
#                 self._z = self.validate_point(z)
#
#     def get_x(self):
#             return self._x
#
#     def get_y(self):
#             return self._y
#
#     def get_z(self):
#             return self._z
#
#     @staticmethod
#     def validate_point(num):
#         return num if type(num) == int else 0
#
# point = Point(2, 10, '456')
# print(point.__dict__, point.get_y())
#
# print(getattr(point, '_y')) # getattr -показывает имя в кот.содержиться в 'y'
#
# setattr(point, '_y', 20) #а даем новое число для 'y'
# print(getattr(point, '_y'))
# print(point.__dict__, point.get_y())
#
# >{'_x': 2, '_y': 10, '_z': 0} 10
# >10
# >20
# >{'_x': 2, '_y': 20, '_z': 0} 20