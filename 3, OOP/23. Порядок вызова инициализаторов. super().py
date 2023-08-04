# Занятие 23. Порядок вызова инициализаторов. super()
# - Расширение и переопределение
# - Class.__init__
# - super()
# Добавляя новый доволнительный класс class Dog(Animal), у нас есть 2 возможности: Расширить и ято-то переопределить.
#     Расширение -это добавление чего-то нового функционала. Мы взяли класс Dog и расширили его методы play_game,
#  do_sound. =# dog.play_game().
#     Переопределение -Это изменение уже сущ-его метода базового класса(родительского) .
# уже сущ-ий метод do_sound мы его переопределяем.

# - super()- это команда ,кот.возвращает нашего родителя

# Порядок (цепочка) вызова
class Animal:
    def __init__(sel):
        print('Animal - __init__')


class Dog(Animal):
    def __init__(self, name):
        super().__init__() #универсальное слово(команда) для ссылки родителя
        print('Dog - __init__')


class Ovcharka(Dog):
    def __init__(self, name):
        super().__init__(name)  #универсальное слово(команда) для ссылки родителя
        print('Ovcharka - __init__')


ovcharka1 = Ovcharka('Жучка')
# # >>Animal - __init__   -->родительский класс (самый-самый верхний класс Object)
# # Dog - __init__          -->дочерний класс
# # Ovcharka - __init__       -->подкласс дочернего
# ----------------------------------
# ссылаемся на имя верхнешл класса.
# class Animal:
#     def __init__(self):
#         print('Animal - __init__')
#
#
# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)   #ссылаеться на родительский класс
#         print('Dog - __init__')
#
#
# class Ovcharka(Dog):
#     def __init__(self ):
#         Dog.__init__(self) #ссылаеться на дочерний класс
#         print('Ovcharka - __init__')
#
#
# ovcharka1 = Ovcharka()
# >>Animal - __init__  # сравнимо с человеком. Тут родился дед
# Dog - __init__          # сравнимо с человеком. Тут родился отец
# Ovcharka - __init__         # сравнимо с человеком. Тут родился сын