

def library(book): # функция принимает параметр func
    def inner(*args, **kwargs): #  тут 2 аргумента, кот.принимают
        print('Ищем новую книгу')
        res = book(*args, **kwargs) #вызов функции, кот. выполняет информацию
        print('Ищем новую книгу')
        return res # возвращает результат

    return inner

@library # декоратор,
def read(roman, detectiv):
    print(f'Я читаю: {roman}, {detectiv}')
    return 'Посещение закрыто'


print(read('Рыбка', 'Я ищу  тебя'))  # функция с декоратором с ссылкой на функции


# Python-код, возвращающий длину строки
def findLen(str):
    if not str:
        return 0
    else:
        some_random_str = 'py'
        return ((some_random_str).join(str)).count(some_random_str) + 1
str = "катерина"

print(findLen(str))






