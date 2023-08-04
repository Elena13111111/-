class Dog:
    animal_type = 'Собака'  #переменные
    legs_num = 4

    def __init__(self, name, age):
        self.name = name  # это переменная в объекте
        self.age = age

    def __str__(self): # переопределение (переменных) в строку. Даем нове значение
        # return f'Dog ({self.name}, {self.age})'
        return f'{Dog.animal_type}\n\tКличка: {self.name} \n\tВозраст: {self.age} \n\tКол-во лап: {self.legs_num}'


dog1 = Dog('Тузик', 4)
dog2 = Dog('Бобик', 10)
# print(dog2.name, dog2.age)
# print(dog1.name, dog1.age)
# print(dog1)
# print(dog2)
print(Dog.animal_type)
print(Dog.legs_num)