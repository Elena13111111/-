# Занятие 25. Data классы
# - Data классы
# - Параметры по умолчанию
# - field(default_factory=list)
# - frozen=True
# - Инкапсуляция и датакласссы. Неизменяемые объекты

# 1.
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     #__repr__ это откладочная информация , оно именно в ПРинтах дается
#     def __repr__(self):
#         return f' Name :{self.name}, Age : {self.age}'
#
#     # __str_ это строковое представление, кот. идет везде
#     def __str__(self):
#         return f' Name :{self.name}, Age : {self.age}'
#
# print(Person('Олег', 56))
# >> Name :Олег, Age : 56
# Ответ будет тот же если мы удалим  def __repr__ или def __str__

# -----------------------------------
# 2. Пример без геттеров и сеттеров
# from  dataclasses import dataclass
#
# #@dataclass 0хранение данных некоторых полей
# #frozen=True - запрещает нам менять данные
# @dataclass(frozen=True)
# class Person: # анотация
#      name : str  # строка  / тип значение
#      age  : int  # число   / тип значение
#
#
# print(Person('Олег', 56))
# # >>Person(name='Олег', age=56)
# print(Person('Олег', 56) == Person('Олег', 56)) #метод сравнения, встроенный метод __eq__
# >>True

# мы могли менять данные, когда не печатали frozen=True
# person = Person('Олег', 56)
# print(person.age)
# person.age = 88
# print(person.age)
# # >>56 (было)
# # 88  (стало)
# print(person.__dict__)
# # >>{'name': 'Олег', 'age': 88}
# # Как правильно переопределять данные сущ-их:
# person2 = Person(person.name,88)
# print(person2)
# # >>Person(name='Олег', age=88)
# _____________________________
# № 3
# from  dataclasses import dataclass
#
#
# @dataclass(frozen=True)
# class Person: # анотация/ параметры по умолчанию
#      name : str  = "Вася"
#      age  : int  = 36
#
# # print(Person('Олег', 56))
# # print(Person())
# # >>Person(name='Олег', age=56)
# # >>Person(name='Вася', age=36)
#
# person = Person('Андрей')
# print(person)
# person2 = Person(person.name , 45)
# print(person2)
# # >>Person(name='Андрей', age=36)
# # >>Person(name='Андрей', age=45)
# print(person)
# person3 = Person('Jane' , 99)
# print(person3)
# # >>Person(name='Jane', age=99)
# ----------------------------------
# № 4
# from  dataclasses import dataclass
#
# @dataclass(frozen=True)
# class Person:
#     name: str
#     childs :[]
#     age: int = 25
#
# person = Person('Андрей',['Ваня'])
# print(person)
# person2 = Person(person.name ,[] , 89)
# print(person2)
# # >>Person(name='Андрей', childs=['Ваня'], age=25)
# # >>Person(name='Андрей', childs=[], age=89)
# ------------------------------------

# № 5 Такой пример неправильный def __init__(self, name, age,childs=[]):
# from  dataclasses import dataclass
#
# class Person:
#     def __init__(self, name, age,childs=[]):
#         self.name = name
#         self.age = age
#         self.childs = childs
#
#     def __repr__(self):
#         return f'name: {self.name}, age: {self.age}'
#
# # @dataclass(frozen=True)
# # class Person:
# #     name: str
# #     age: int
# #     childs: list = field(default_factory=list)
#
# person = Person('Андрей',27)
# print(person)
# person2 = Person(person.name , 89)
# print(person2)
# # >>name: Андрей, age: 27
# # >>name: Андрей, age: 89
#
# person.childs.append('Сын1')
# person2.childs.append('Сын2')
# print(person2.childs)
# >>['Сын1', 'Сын2']
# ______________________
# № 6  пример
from  dataclasses import dataclass, field
 # class Person:
 #    def __init__(self, name, age):
 #        self.name = name
 #        self.age = age
 #
 #    def __repr__(self):
 #        return f'name: {self.name}, age: {self.age}'

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    childs: list = field(default_factory=list)
    #field(default_factory=list) -задает данные для каждого объекта

person = Person('Андрей',27)
print(person)
person2 = Person(person.name , 89)
print(person2)
# >>name: Андрей, age: 27
# >>name: Андрей, age: 89

person.childs.append('Сын1')
person2.childs.append('Сын2')
print(person.childs)
print(person2.childs)
# >>['Сын1']
# ['Сын2']
print(person)
print(person2)
# >>Person(name='Андрей', age=27, childs=['Сын1'])
# >>Person(name='Андрей', age=89, childs=['Сын2'])