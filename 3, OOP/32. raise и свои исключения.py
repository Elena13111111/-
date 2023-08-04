# Занятие 32. raise и свои исключения
# - Где можно отлавливать исключения
# - raise
# - Свои исключения

# traceback - Исключения, программа показывает путь ошибки по цепочке
# - raise- поднять ошибки без ее создания


# import traceback
#
#
# def run_light():
#     1 / 0                #тут ошибка
#     print('Свет включён')
#
#
# def start_lightning():
#     print('Умный дом включен 2 ')
#     run_light()
#
# def run():
#     print('Умный дом включен 1 ')
#     start_lightning()
#
# try:          # это позволяет отловить ошибку и дать проге дальше работать
#     run()
# except Exception as e:
#     traceback.print_exc()   # эта функция показывает какая ошибка была
#
# print('Программа продолжает работать')

# >>Умный дом включен 1
# Умный дом включен 2
# Программа продолжает работать
# >>Traceback и 4 ссылки
# >> ZeroDivisionError: division by zero
--------------------------
class CustomException(Exception):
    pass
    """Ошибка для таких-то случаев"""


try:
    raise CustomException('Какая-то ошибка') #пишеться внутри Ошибок
except Exception as e:
    print('Ошибка обработана')
#>> Ошибка обработана

