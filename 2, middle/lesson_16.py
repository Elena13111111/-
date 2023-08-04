#pip install XlsxWriter

import xlsxwriter
import datetime


date_now = datetime.datetime.now()
students = {
    'Петров': {
        'Математика': [
            (date_now - datetime.timedelta(days=5), 9),  # дата сейчас -5дней, 9 оценка
            (date_now - datetime.timedelta(days=3), 3),  # дата сейчас -3дня, 3 оценка
            (date_now, 8)
        ],
        'Физика': [
            (date_now - datetime.timedelta(days=10), 5),
            (date_now - datetime.timedelta(days=3), 7),
            (date_now, 8)
        ]
    },
    'Сидорова': {
        'Математика': [
            (date_now - datetime.timedelta(days=5), 6),
            (date_now - datetime.timedelta(days=3), 8),
            (date_now, 8)
        ],
        'Физика': [
            (date_now - datetime.timedelta(days=10), 3),
            (date_now - datetime.timedelta(days=3), 7),
            (date_now - datetime.timedelta(days=1), 8),
            (date_now, 10),
        ]
    }
}
# создание файла
workbook = xlsxwriter.Workbook('../venv/test_file.xlsx')
worksheet = workbook.add_worksheet('Петров') # имя файла
bold = workbook.add_format({'bold': True})  # жирный текс, Переменная
worksheet.write('A1', 'Дата', bold)    #название столбцов
worksheet.write('B1', 'Математика', bold)
worksheet.write('C1', 'Физика', bold)


# Запись дат
worksheet.write('A2', str(date_now - datetime.timedelta(days=10))[:10]) # берем первык 10 символов
worksheet.write('A3', str(date_now - datetime.timedelta(days=5))[:10])
worksheet.write('A4', str(date_now - datetime.timedelta(days=3))[:10])
worksheet.write('A5', str(date_now)[:10])

# Запись отметок. Математика
worksheet.write('B2', 9)
worksheet.write('B3', 3)
worksheet.write('B4', 8)


# Запись отметок. Физика
worksheet.write('C2', 5)
worksheet.write('C4', 7)
worksheet.write('C5', 8)

workbook.close()