# Занятие 30. Отличия Атрибутов класса и Атрибутов объекта
# - Атрибуты класса / объекта
# реопределение тех и других
# - Общий список атрибутов класса

# два атрибута находяться на разных местах
# class Person:
#     name = None      #это атрибуса класса /они имеют одни и те же данные для всех класса
#     def __init__(self, name2, age):
#         self.name = name2     #это атрибуса объекта
#         self.age = age
#
#     def __repr__(self):
#         return f' {self.name} {self.age}'
#
# # print(Person('Василий', 27))
# # >>  Василий 27
#
# person1 = Person('Андрей', 48)
# print(person1)
# person2 = Person('Василий', 28)
# print(person2)
# print(person1)   # не поменялось
#>> Андрей 48
# Василий 28
# Андрей 48
# ----------------------------

class Person:
    MIN_AGE = 0    #это атрибуса класса общие /они имеют одни и те же данные для всех класса
    MAX_AGE = 99
    data = []

    def __init__(self, name2, age):
        self.name = name2     #это атрибуса объекта
        self.age = age

    def __repr__(self):
        return f' {self.name} {self.age}'

# print(Person('Василий', 27))
# >>  Василий 27

person1 = Person('Андрей', 48)
print(person1)
person2 = Person('Василий', 28)
print(person2)
print(person1)

# print(person1.__dict__)
# print(Person.__dict__)

# >>{'name': 'Андрей', 'age': 48}
# {'__module__': '__main__', 'name': 'Андрей', '__init__': <function Person.__init__ at 0x0000021322159EE0>, '__repr__': <function Person.__repr__ at 0x0000021322159F80>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}

print('=' * 120)
person1.data.append('1')
person1.data.append('2')
person1.data.append('3')
print(person1.data)
print(person2.data)

# >> Андрей 48
#  Василий 28
#  Андрей 48
# ===========================================================
# ['1', '2', '3']
# ['1', '2', '3']


