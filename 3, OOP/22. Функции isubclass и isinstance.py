# Занятие 22. Функции isubclass и isinstance
# - issubclass
# - isinstance
# - __name__
# - Наследование базового класса int

#это родительский класс
class Animal:
    def __init__(self, name): # данные - имя
        self.name = name

    def do_sound(self): # звук животного
        print('звук животного')

    def get_name(self):  #тут могут храниться данные наследников
        print(f'Меня зовут: {self.name}')


#это дочерний класс
class Dog(Animal): #class Dog наследует данные от родителя class Animal

    def do_sound(self):
        print('Собака лает Гав-Гав')

    def play_game(self):
        print('Я собака, я несу палку')

class Ovcharka(Dog): #наследуем данные от класса Dog и Animal , получаеться цепочка
    def ovcharka_method(self):
        print('Метод только для овчарок')

# print(Animal.__name__) #имя нашего класса
# # >>Animal
# print(Dog.__name__)
# # >>Dog
# print(Ovcharka.__name__)
# # >>Ovcharka
# print(object.__name__) #Это тоже классы class object:
# # >> object
# print(str.__name__)  #Это тоже классы наследуется от class str(object):
# # >>str
# print(int.__name__)  #Это тоже классы class int(object):
# >>int

# Какой подкласс наследует от кого-то класс? issubclass - Эта функция для сравненеия КЛАССОВ
# print(issubclass(Ovcharka,Dog)) #подкласс Ovcharka явля-ся класс Dog
# # >>True
# print(issubclass(Ovcharka,Animal)) #подкласс Ovcharka явля-ся класс Animal
# # >>True
# print(issubclass(Dog,Ovcharka)) #подкласс Dog явля-ся класс Ovcharka
# >>False

# Функция для сравнения объектов класса
# dog1 = Dog('Тузик') #проверяем явл-ся ли 'Тузик' наследником класса
# print(isinstance(dog1, object))
# # >>True
# print(isinstance(dog1, Dog))
# # >>True
# print(isinstance(dog1, Ovcharka))
# >>False

class superInt(int):
    def __str__(self):
        return f'[{self.real}]'

print(superInt(22) + superInt(3))
# >>25