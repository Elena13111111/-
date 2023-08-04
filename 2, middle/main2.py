import xlsxwriter
import random

# магазин продуктов

#данные о продуктах, 3 вида
product = {
    'фрукты': {
        'заграничные':[
            ('манго', 10 ), # название / кг
            ('папайя', 15 ),
            ('ананас', 20 ),
            ('бананы', 30)
            ],
        'свои':[
            ('яблоки', 50),
            ('груши', 80),
            ('персики', 40),
            ('вишня', 60)
        ]
    },
    'овощи': {
        'заграничные':[
            ('Кивано', 10 ), # название / кг
            ('Мелотрия', 15 ),
            ('Огурдыня', 20 ),
            ('Разноцветная кукуруза', 30)
        ],
        'свои':[
            ('свекла', 45),
            ('капуста', 55),
            ('огурцы', 100),
            ('помидоры', 90)
        ]
    },
'орехи': {
        'заграничные':[
            ('пекан', 14 ), # название / кг
            ('Макадамия', 19 ),
            ('Бразильский', 20 ),
            ('Мускатный', 18)
        ],
        'свои':[
            ('грецкие', 108),
            ('фундук', 98),
            ('миндаль', 78),
            ('кедровые', 66)
        ]
    }
    }

#создание файла
workbook = xlsxwriter.Workbook('main2.xlsx')
worksheet = workbook.add_worksheet('фрукты') #старница 1
bold = workbook.add_format({'bold': True})  # жирный текс, Переменная

worksheet.write('B1:C1', 'Заграничные', bold)    #название столбцов
worksheet.write('A2', '№ отдела', bold)    #название столбцов
worksheet.write('B2', 'Название продукта', bold)
worksheet.write('C2', 'кг', bold)

worksheet.write('B8:C8', 'Свои', bold)    #название столбцов
worksheet.write('A9', '№ отдела', bold)    #название столбцов
worksheet.write('B9', 'Название продукта', bold)
worksheet.write('C9', 'кг', bold)

# столбец заграничные кг
worksheet.write('C3', 10)
worksheet.write('C4', 15)
worksheet.write('C5', 20)
worksheet.write('C6', 30)

# столбец заграничные название
worksheet.write('B3', 'манго')
worksheet.write('B4', 'папайя')
worksheet.write('B5', 'ананас')
worksheet.write('B6', 'бананы')

# столбец свои кг
worksheet.write('C10', 50)
worksheet.write('C11', 80)
worksheet.write('C12', 40)
worksheet.write('C13', 60)

# столбец свои название
worksheet.write('B10', 'яблоки')
worksheet.write('B11', 'груши')
worksheet.write('B12', 'персики')
worksheet.write('B13', 'вишня')

otdel =random.randint(1,10)

# Запись дат привоза продуктов Заграничных
worksheet.write('A3',f' Отдел:{otdel}' )
worksheet.write('A4',f' Отдел {otdel}' )
worksheet.write('A5',f' Отдел {otdel}' )
worksheet.write('A6',f' Отдел {otdel}' )

otdel =random.randint(11,20)
# Запись дат привоза продуктов Свои
worksheet.write('A10',f' Отдел {otdel}' )
worksheet.write('A11',f' Отдел {otdel}' )
worksheet.write('A12',f' Отдел {otdel}' )
worksheet.write('A13',f' Отдел {otdel}' )



workbook.close()


#worksheet = workbook.add_worksheet('овощи') #старница 2
#worksheet = workbook.add_worksheet('орехи') #старница 3

