
class Str_animal: # Этот дексприптор.
    @staticmethod
    def validate_animal(name_animal):
        return name_animal if type(name_animal) == str else 0
    # возвращаем ИМЯ равное строковому значению, иначе 0

    # э то 3метода кот. всегда присутствуют.owner не трогаем

    def __set_name__(self, owner, name): #  имя переменных
        self.name = '....' + name  #новое имя, кот. мы задаем

    def __get__(self, instance, owner):  # геттер.
        return getattr(instance, self.name) #instance - объект

    def __set__(self, instance, value):  # сеттер
        setattr(instance, self.name, self.validate_animal(value)) # проверка на число

class Animal:
    cat = str_animal()
    dog = str_animal()
    bird =str_animal()

    def __init__(self, cat, dog, bird): # передаем координаты
        self.cat = cat
        self.dog = dog
        self.bird = bird


point1 = Animal('сиямская','бульдог' , 'аист')
point2 = Animal('сфинкс', 'Шитсцу', 'Голубь')
print(point1.__dict__)
print(point2.__dict__)
#>> {'....cat': 'сиямская', '....dog': 'бульдог', '....bird': 'аист'}
#>> {'....cat': 'сфинкс', '....dog': 'Шитсцу', '....bird': 'Голубь'}
print(point2.cat)
point2.cat = "Мейн-кун" # меням число на другое
print(point2.cat)
print(point2.__dict__)
# >>сфинкс
# >>Мейн-кун
# >>{'....cat': 'Мейн-кун', '....dog': 'Шитсцу', '....bird': 'Голубь'}



