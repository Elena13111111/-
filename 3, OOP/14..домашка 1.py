# библиотека



# 1. Пример.
def library(book): # функция принимает параметр book
    def inner(*args, **kwargs): #  тут 2 аргумента, кот.принимают
        print('Ищем новую книгу')
        res = book(*args, **kwargs) #вызов функции, кот. выполняет информацию
        print('Ищем новую книгу')
        return res # возвращает результат

    return inner

@library # декоратор,
def read(book1, book2):
    print(f'Я читаю: {book1}, {book2}')
    return 'Посещение закрыто'


print(read('Рыбка', 'Я ищу  тебя'))  # функция с декоратором с ссылкой на функции


# >>Ищем новую книгу
# Я читаю: Рыбка, Я ищу  тебя
# Ищем новую книгу
# Посещение закрыто
#
#  ---------------------------------------------------------------------
# 2.Пример.
# def library(min_num, max_num):
#     def decorator(func):  # функция для декоратора мин и мах
#         def inner(*args, **kwargs):
#             new_args = []
#             for arg in args:  # проверка чисел
#                 new_arg = None
#                 if type(arg) == int and min_num <= arg <= max_num:  # если тип ЧИСЛОВОЕ и от мин до мах
#                     new_arg = arg
#                 new_args.append(new_arg)
#             res = func(*new_args, **kwargs)
#             return res
#         return inner
#     return decorator  # функция для декоратора мин и мах
#
# #имя
# def name(first_name, last_name):
#     print(f' Внимание, в зале тишина!')
#     print(f' Читатель : {first_name},{last_name} Приветствуем вас')
#
# # чит.билет
# @library(min_num=1, max_num=20)
# def readers(num1, num2 ):
#         print(f'Ваш читательский билет {num1}, и номер книги {num2}')
#
# print('Добро пожаловать!')
# print('=' * 90)
#
# name ('Виктор', 'Кошкин')
# readers(10, 15)
# name ('Ольга', 'Овечкина')
# readers(-1, 35)
# name ('Петр', 'Ложкин')
# readers('8', 569)
#
# print('=' * 90)
# print('Библиотека закрыта для посещений!')







