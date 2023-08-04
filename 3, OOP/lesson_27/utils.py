#утилитные функции

import random


class Utils: # базовые константы
    ADMIN_ACCESS = 'ADMIN_ACCESS'
    STUDENT_ACCESS = 'STUDENT_ACCESS'

# функция для ввода пароля и логина
    @staticmethod
    def input_login_pass():
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        return login, password   #возвращаем логин и пароль

#функция проверки Регистрации
    @staticmethod
    def check_is_registered(students, login, password): #проходим по студентам, и у нас есть логин и пароль
        res = None        # результат изначльно равен НЕТУ
        if login.lower() in students.keys():  #если из логина (мал.буквы) в списке студентов.ключ
            student = students[login.lower()]   # студент = верному логину
            valid_password = student.password    # а пароль равен верному паролю
            if password == valid_password: # если пароль равен введенному пароли
                res = student             # результат = один студент
        return res                       # то возвращаем результат


# функция  для генерации теста
    @staticmethod
    def generate_random_test():
        number1 = random.randint(1, 10)
        znak = ['-', '+', '*'][random.randint(0, 2)]
        number2 = random.randint(1, 10)
        question = f'{number1} {znak} {number2}'
        return question, eval(question)

    @staticmethod
    def start_viktorina(student):   # начало викторины для студента

        # q1 = ["История. В каком году закончилась Великая Отечественная война? ", "1945"]
        # q2 = ["Геометрия. Как называется треугольник у которого все стороны равны? ", "Равносторонний"]
        # q3 = ["Биология. Как называется процесс синтеза углеводов из неорганических веществ за счёт энергии солнца? ",
        #       "фотосинтез"]
        # q4 = ['Кто является самой большой кошкой на планете?','Тигр']
        # q5 = ['Какая птица самая маленькая?','Колибри']


        kol = 0
        vsego = 5

        otv = input("История. В каком году закончилась Великая Отечественная война? ")
        if otv == "1945":
            print("Верно")
            kol = kol + 1
        else:
            print("Не верно")

        otv = input("Геометрия. Как называется треугольник у которого все стороны равны? ")
        if otv.lower() == "равносторонний":
            print("Верно")
            kol = kol + 1
        else:
            print("Не верно")

        otv = input( "Биология. Как называется процесс синтеза углеводов из неорганических веществ за счёт энергии солнца? ")
        if otv.lower() == "фотосинтез":
            print("Верно")
            kol = kol + 1
        else:
            print("Не верно")

        otv = input(" Кто является самой большой кошкой на планете?")
        if otv.lower() == "тигр":
            print("Верно")
            kol = kol + 1
        else:
            print("Не верно")

        otv = input("Какая птица самая маленькая?")
        if otv.lower() == "колибри":
            print("Верно")
            kol = kol + 1
        else:
            print("Не верно")

        print(kol, " верных ответов из ", vsego)
