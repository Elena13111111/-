# Создайте новый файл Excel и добавьте рабочий лист.
workbook = xlsxwriter.Workbook('text_file.xlsx')
worksheet = workbook.add_worksheet()

# Увеличьте первый столбец, чтобы сделать текст более понятным.
worksheet.set_column('A:A', 20)

# Добавьте жирный шрифт, который будет использоваться для выделения ячеек.
bold = workbook.add_format({'bold': True})

# Напишите какой-нибудь простой текст.
worksheet.write('A1', 'Hello')

# Текст с форматированием.
worksheet.write('A2', 'World', bold)

# Напишите несколько чисел с обозначением строк / столбцов.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

workbook.close()