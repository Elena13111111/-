import random
import main2
import xlsxwriter
import pandas
import os
import datetime
import openpyxl

#закупка продуктов. Права покупателя. Права Админа.

# уровень доступа
ADMIN_ACCESS = 'ADMIN_ACCESS'   #админ
BUYER_ACCESS = 'BUYER_ACCESS'   #покупатель
NO_ACCESS = 'NO_ACCESS' # нет доступа
POKUPKI = 'pokupki.xlsx'

logins = {
    'admin': ('123', ADMIN_ACCESS),  # логин : пароль, (уровень доступа) Админ
    'ма': ('123', BUYER_ACCESS),
    'соня': ('123', BUYER_ACCESS),
    'валера': ('123', BUYER_ACCESS),
    'костя': ('123', BUYER_ACCESS)

}
MENU = {
    ADMIN_ACCESS: {    # права для админа
        1: 'Посмотреть Баллы покупателя',
        2: 'Посмотреть информацию о покупателе',
        10: 'Выйти'
    },
    BUYER_ACCESS: {   # права для покупателя
        1: 'Сыграть в лотерею',
        2: 'Купить продукты из списка',
        10: 'Выйти и сохраниться'
    }
}

product= {
    1: 'манго',
    2: 'папайя',
    3: 'ананас',
    4: 'бананы',
    5: 'яблоки',
    6: 'груши',
    7: 'персики',
    8: 'вишня'
}


buyer = {}

# для ввода логина и пароля
def check_is_registered(): # проверяем регистрацию
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    if login.lower() in logins.keys(): # если Логин находится в словаре Ключя,
        valid_password = logins[login.lower()][0]    # то доступ открыт
        if password == valid_password:    # если правильный пароль
            return logins[login.lower()][1], login    # доступ открыт, роль и логин
        else:
            return NO_ACCESS, login    # когда нет доступа, неправильно ввел логин
    else:
        return NO_ACCESS, login
    # return check_is_registered()
    while True:
        print(check_is_registered())


 #меню выбора
def show_menu(access_role, login):
    while True:
        current_menu = MENU[access_role]
        print(current_menu)
        chosen_item = int(input('Выберите пункт меню: '))
        if access_role == BUYER_ACCESS and chosen_item == 1: # вызов пункта для покупателя
            by_loterea(login)
        elif access_role == BUYER_ACCESS and chosen_item == 2:  # вызов пункта для покупателя
            by_product(login)
        elif access_role == ADMIN_ACCESS and chosen_item == 10: # вызов пункта для админа
            print('Программа заверишила работу')
            return show_menu()
        elif access_role == ADMIN_ACCESS and chosen_item == 2: # вызов пункта для админа
            show_buyer_info()
        elif access_role == BUYER_ACCESS and chosen_item == 10:
            print('Все данные успешно сохранены')
            save_data()
            return check_is_registered()

#лотерея пример
def lotereia():
    number1 = random.randint(1, 10)
    znak = ['+','*','-'][random.randint(0, 2)]
    number2 = random.randint(1, 10)
    otvet = f'{number1} {znak} {number2}'
    return otvet, eval(otvet)


#лотерея
def by_loterea(login):
       buyer_answer=0
       for i in range(1, 5):   #выбрать 4 примера
           try:  # если ответ правильный, то след-ий пример
               otvet, answer = lotereia()
               print(f" Реши пример и собирайте баллы :{otvet}")
               user_answer = int(input('Ваш ответ: '))
               if answer == user_answer:
                  buyer_answer += 1
           except Exception as e:  # если ответ неверный,
                print('Вы ввели ерунду и потеряли шанс получить баллы')

       #баллы за ответы
       balli = buyer_answer *3
       if login in buyer:
           buyer[login].append(buyer,balli)
       else:
           buyer[login]=[(buyer, balli)]

       print(f'Вы набрали баллы: {balli}')


#сохрание данных
def save_data():
    workbook = xlsxwriter.Workbook(POKUPKI)
    bold = workbook.add_format({'bold': True})
    for buyer_1, product in buyer.items():
        worksheet = workbook.add_worksheet(buyer_1)
        worksheet.write('A1', 'Покупатель', bold)
        worksheet.write('B1', 'баллы', bold)
        counter = 2
        for i in balli:
            worksheet.write(f'A{counter}', str(i[0]))
            worksheet.write(f'B{counter}', i[1])
            counter += 1

    for product_fr, kg in buyer.items():
        worksheet = workbook.add_worksheet(product_fr)
        worksheet.write('D1', 'Продукт', bold)
        worksheet.write('F1', 'кг', bold)
        counter = 2
        for m in product_fr:
          worksheet.write(f'D{counter}', str(m[0]))
          worksheet.write(f'F{counter}', m[1])
          counter += 1

    workbook.close()


#Купить продукты из списка
def by_product(login):
    print(f'{product}')
    vibor_roducta= (int(input(f'Вы выбрали № : ')))
    vibor_kg= int(input('Введите кол-во кг:'))
    vibor_final= (f'Вы выбрали номер продукта:{vibor_roducta} на {vibor_kg} кг')
    print(vibor_final)


#информация о покупателе
def show_buyer_info():
    buyer_name = input('Введите имя покупателя: ')
    if buyer_name in logins.keys():
        to_print = f'Все баллы покупателя: {buyer_name}\n'
        balli = buyer[buyer_name]
        to_print2= f'Все покупки покупателя: {buyer_name}\n'
        by_product= buyer[buyer_name]
        for counter, balli in enumerate(balli):
            to_print  += f'{counter}. {balli[1]}  ->  {balli[0]}\n'
            to_print2 += f'{counter}. {by_product[1]}  ->  {by_product[0]}\n'
        print(to_print)
        print(to_print2)
    else:
        print(f'Покупатель с именем {buyer_name} не существует')

def load_buyer():
    if os.path.exists(POKUPKI):
        xlsx_data = pandas.ExcelFile(POKUPKI)    #читаем наш файл
        for sheet in xlsx_data.sheet_names:    # подгружаем имя покупателя и его страница
            df1 = pandas.read_excel(xlsx_data, sheet)
            balli = df1.values.tolist()        # баллы
            buyer[sheet] = list(      #покупатель, их страница = лист с баллами
                map(                       #приобразуем строку
                    lambda el:
                    ( buyer , balli )))

 #  запуск программы
def run_study_program():
    access_role, login = check_is_registered()
    if access_role != NO_ACCESS:
        show_menu(access_role, login)
    else:
        print('Ты не смог залогиниться в программе')

        return run_study_program()

run_study_program()