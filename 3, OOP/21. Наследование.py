# Занятие 21. Наследование
# - Наследование Общий принцип
# - Вызов в Родителе методов дочернего класса
# - Переопределение атрибутов и методов

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
    # def __init__(self, name):  # данные - имя
    #     self.name = name
# мы убираем одинаковый код  def __init__, т.к. он есть в class Animal .

    def do_sound(self):
        print('Собака лает Гав-Гав')

    def play_game(self):
        print('Я собака, я несу палку')

class Ovcharka(Dog): #наследуем данные от класса Dog и Animal , получаеться цепочка
    def ovcharka_method(self):
        print('Метод только для овчарок')


# animal = Animal('Неопознаное животное')
dog = Dog ("Собака Вася")
# dog = Ovcharka ('уф- уф') #2вариант

# animal.do_sound()
# animal.get_name()
# >>Звук животного
# >>Меня зовут: Неопознаное животное

# dog.play_game()
# >>Я собака, я несу палку
# dog.get_name(), dog.do_sound(), dog.play_game()
# #>> Меня зовут: Собака Вася
# # Собака лает Гав-Гав
#  Я собака, я несу палку
# dog.ovcharka_method()
# >>Метод только для овчарок
# dog.get_name()
#>Меня зовут: уф- уф
dog1 =Ovcharka('Собака федя')
dog1.get_name()
dog1.do_sound()
# >>Меня зовут: Собака федя
# Собака лает Гав-Гав


