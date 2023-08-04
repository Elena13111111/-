class Dog:
    __MIN_AGE = 0 #делаем параметры диапазона возраста собак. Это константа , потому большие буквы
    __MAX_AGE = 35
    __MIN_NAME_LEN = 3

    @classmethod  #будет проверять возраст
    def __check_age(cls, age):
        if type(age) != int: # если что-то делаем не корректно. Если возраст не число
            raise TypeError (f'Вы ввели : {age} .Возраст имеет только ЧИСЛОВОЕ значение ')
            #  raise -это 'ошибка'
        elif not  cls.__MIN_AGE <= age <= cls.__MAX_AGE: # от 0 до 35 возвраст ограничим
            raise TypeError(f'Возраст в диапазоне :от ({cls.__MIN_AGE}) до ({cls.__MAX_AGE}) ')

    @classmethod   #будет проверять имя
    def __check_name(cls, name):
        if type(name) != str: #если имя НЕ строка
            raise TypeError (f'Вы ввели :{name}.ИМЯ Разрешено писать только строкой или в кавычках ' ' ')
        elif  len(name) < cls.__MIN_NAME_LEN: # если имя меньше 3 символов
            raise  TypeError (f'Вы ввели :{name}, исп-уйте минимум {cls.__MIN_NAME_LEN} символов ')

    def __init__(self, name, age):# это переменная в объекте
        self.__check_age(age)  #проверка на правильность  'Возраста'
        self.__check_name(name)#проверка на правильность  ИМя
        self.name = name
        self.age = age

    @property #геттер
    def name(self):
        return self.__name
    @name.setter # сеттер (первое пишем из геттера name и обозначаем сеттер)
    def name(self, name):
        self.__check_name(name)
        self.__name = name

    @property  # геттер
    def age(self):
        return self.__age
    @age.setter # сеттер (первое пишем из геттера age и обозначаем сеттер)
    def age(self, age):
        self.__age = age
        self.__check_age(age) #проверка

dog1 = Dog('Тузик', 4)

print(dog1.name, dog1.age)
dog1.name='Бобик'
dog1.age=33
print(dog1.name, dog1.age)
