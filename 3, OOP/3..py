class Cat: # пишем класс Cat, это шаблон Кота, не сущ-ий объект
    def __init__(self, name='Кот', age=1): # параметры по умолчанию
        self.name = name #передаем параметры
        self.age = age
       # print(f'Кот {self.name} родился')

    def __del__(self):
        print(f'Кот {self.name} ушел')


cat1=Cat('Вася', 6)
cat2=Cat('Мурка', 2)
cat3=Cat()
cat2=Cat()
#
# print(cat1.name)
# print(cat2.name)
# print(cat3.name)

# cat4= {
# 'name': 'Василий',
#     'age': 2
#     }
#
# print(cat1.__dict__)
# print(cat4)