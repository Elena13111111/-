# 1. Регистрация и вход в приложение по паролю и логину
# 2. Решение задач и получениб отметок
# 3. Сохрание slx в журнал отметок.
# 4. Функции для статистики по ученикам для администратора. Подсчет среднего балла:
#     а) по предмету.
#     б) по дате .
#     в) по дате и предмету.

# +1. Регистриация и вход в прилжение по логину и паролю
# +2. Решение тестов и получение отметок
# +3. Сохранение в xls журнала отметок
# -4. Функции для статистики по ученикам для администратора
# -а) Средний бал всех учеников и общий средний балл по школе
# -б) Перечень всех отметок по ученику
# -5. Подргузка отметок при запуске

import datetime
import random
import xlsxwriter

# уровень доступа
ADMIN_ACCESS = 'ADMIN_ACCESS'
STUDENT_ACCESS = 'STUDENT_ACCESS'
INVALID_CREDENTIALS = 'INVALID_CREDENTIALS' # нет доступа

logins = {
    'admin': ('12345', ADMIN_ACCESS),  # логин : пароль, (уровень доступа) Админ
    'мария': ('12345', STUDENT_ACCESS),
    'иван': ('12345', STUDENT_ACCESS),
    'гоша': ('12345', STUDENT_ACCESS)
}
MENU = {
    ADMIN_ACCESS: {    # права для админа
        1: 'Посмотреть статистику 1',
        2: 'Посмотреть статистику 2',
        10: 'Выйти'
    },
    STUDENT_ACCESS: {   # права для студента
        1: 'Пройти тест',
        2: 'Посмотреть свои отметки',
        10: 'Выйти и сохраниться'
    }
}
# упрощаем оценку
students = {}
    # 'Петров': [( datetime.datetime.now(), 9)]


# для ввода логина и пароля
def check_is_registered(): # проверяем регистрацию
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    if login.lower() in logins.keys(): # если Логин находится в словаре Ключя,
        valid_password = logins[login.lower()][0]    # то доступ открыт
        if password == valid_password:    # если правильный пароль
            return logins[login.lower()][1], login    # доступ открыт, роль и логин
        else:
            return INVALID_CREDENTIALS, login    # когда нет доступа, неправильно ввел логин
    else:
        return INVALID_CREDENTIALS, login
    return check_is_registered()

# рандомный тест для студента
def generate_random_test():
    number1 = random.randint(1, 100)
    znak = ['-', '+', '*' ][random.randint(0, 2)] # берет рандомный знак до 3 возможных
    number2 = random.randint(1, 100)
    question = f'{number1} {znak} {number2}'
    return question, eval(question)  #калькулятор решений
           # вопрос, ответ


def start_test(login):
    right_answers = 0 # изначально ответов у нас ноль
    for i in range(1, 6):    # от 1 до 6 примеров надо решить (5 шт)
        question, answer = generate_random_test()
        print(f'Реши пример: {question}')  # пишем для себя сразу ответ ,eval(question)
        user_answer = int(input('Ваш ответ: '))
        if answer == user_answer:       # если правильный ответ
            right_answers += 1           # добавляем один балл

    mark = right_answers * 2     # оценка умножить на 2 балла
    if login in students:
        students[login].append((datetime.datetime.now(), mark))  #по логину, кладем время и оценку
    else:
        students[login] = [(datetime.datetime.now(), mark)]  #если нету оценку, создаем новый список время и отметка
    print(f'Твоя отметка: {mark}')


 # сохраняем данные в файл ексель
def save_data():
    workbook = xlsxwriter.Workbook('marks.xlsx')
    bold = workbook.add_format({'bold': True})
    for student, marks in students.items():      # ключ : значение
        worksheet = workbook.add_worksheet(student)  #страница мария
        worksheet.write('A1', 'Дата', bold)
        worksheet.write('B1', 'Отметка', bold)
        counter = 2
        for mark in marks:
            worksheet.write(f'A{counter}', str(mark[0]))  # дата отметка, приобразование в строку
            worksheet.write(f'B{counter}', mark[1])   # отметка
    workbook.close()

 #меню выбора
def show_menu(access_role, login):
    while True:
        current_menu = MENU[access_role]
        print(current_menu)
        chosen_item = int(input('Выберите пункт меню: '))
        if access_role == STUDENT_ACCESS and chosen_item == 1: # вызов пункта для студента
            start_test(login)
        elif access_role == ADMIN_ACCESS and chosen_item == 10: # вызов пункта для админа
            print('Программа заверишила работу')
            return show_menu()
        elif access_role == STUDENT_ACCESS and chosen_item == 10:
            print('Все данные успешно сохранены')
            save_data()
            return check_is_registered()

 #  запуск программы
def run_study_program():
    access_role, login = check_is_registered()
    if access_role != INVALID_CREDENTIALS:
        show_menu(access_role, login)
    else:
        print('Ты не смог залогиниться в программе')

        return run_study_program()

run_study_program()



