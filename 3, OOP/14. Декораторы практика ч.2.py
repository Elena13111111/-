# Занятие 14. Декораторы практика ч.2
# - Декоратор для валидации параметров
# - Декоратор с аргументами
import  time

def validate_age(age):
    res_age = None #результат равен None
    if type(age) == int:  #если это явл-ся число
        res_age = age
    return res_age

print(validate_age(10))
print(validate_age('142'))
print(validate_age('dfg'))

>>10
>>None #валидаци. ответ не явл-ся числом
>>None

# ________________________________
def validate_age(min_age, max_age): #валидация
    def decorator(func): #функция для декоратора мин и мах
        def inner(*args, **kwargs):
            new_args = []
            for arg in args: #проверка чисел
                new_arg = None
                if type(arg) == int and min_age <= arg <= max_age: #если тип ЧИСЛОВОЕ и от мин до мах
                    new_arg = arg
                new_args.append(new_arg)
            res = func(*new_args, **kwargs)
            return res

        return inner
    return decorator #функция для декоратора мин и мах

@validate_age(min_age=1, max_age=90) # декоратор
def register_age(age1, age2):
    print('Загружаем информацию')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('..')
    time.sleep(0.5)
    print('..')
    time.sleep(0.5)
    print('...')
    time.sleep(0.5)
    print('....')
    print(f'Возраста {age1}, {age2} сохранён в базу данных')


register_age(0, 5)
register_age(6, 800)
register_age(20, 10)
register_age(-3, 95)

>>Загружаем информацию
.
..
..
...
....
Возраста None, 5 сохранён в базу данных
Загружаем информацию
.
..
..
...
....
Возраста 6, None сохранён в базу данных
Загружаем информацию
.
..
..
...
....
Возраста 20, 10 сохранён в базу данных
Загружаем информацию
.
..
..
...
....
Возраста None, None сохранён в базу данных


