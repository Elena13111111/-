
# заменяем символы на слова во всем коде
STATUS_CONTINUE = 'Игра продолжается'
EMPTY = '_'
ROW1 = '1'
ROW2 = '2'
ROW3 = '3'
COL_A = 'a'
COL_B = 'b'
COL_C = 'c'

data={
     ROW1 : {
         COL_A  : EMPTY,
         COL_B : EMPTY,
         COL_C : EMPTY,
    },
    ROW2: {
        COL_A : EMPTY,
        COL_B: EMPTY,
        COL_C: EMPTY,
    },
    ROW3: {
        COL_A : EMPTY,
        COL_B: EMPTY,
        COL_C: EMPTY
    }
    }
# разрешенные символы, кот.вводим
allowed_symbols = ['X', 'O']
# разрешенные строки, кот.вводим
allowed_rows = [ROW1, ROW2, ROW3]
# разрешенные буквы, кот.вводим
allowed_cols= [COL_A , COL_B, COL_C]




# остановки игры до Победы
def game_end():
    winner = STATUS_CONTINUE

    # кол-во символов по умолчанию их 9, клеток, начинаем с нуля, потом проверим их.
    emty_symbols = 0
    for dat in data.values(): # переменная dat - значение из первой строки
        for d in dat.values():   # наше  значение кладем в переменную d
            if d == EMPTY:       #если переменная d равна пустой строке
                emty_symbols += 1 #тогда пустая клетка прибавляется +1

# Условия игры:
# 1. Заполнены по 3 символа: строка /столбец /диагональ.
# 2. Победа одного игрока.
    # 1=2=3 три одинаковые и 'а' не равна пустому символу, 3 условия в скобках. по горизонтали
    if (data [ROW1][COL_A ] == data [ROW1][COL_B]) and (data [ROW1][COL_A ] == data [ROW1][COL_C]) and (data [ROW1][COL_A ] != EMPTY):
        winner = data [ROW1][COL_A ]
    elif (data[ROW2][COL_A ] == data[ROW2][COL_B]) and (data[ROW2][COL_A ] == data[ROW2][COL_C]) and (data[ROW2][COL_A ] != EMPTY):
        winner = data[ROW2][COL_A ]
    elif (data[ROW3][COL_A ] == data[ROW3][COL_B]) and (data[ROW3][COL_A ] == data[ROW3][COL_C]) and (data[ROW3][COL_A ] != EMPTY):
        winner = data[ROW3][COL_A ]

    # a=b=c три одинаковые и ROW1 не равна пустому символу, 3 условия в скобках. по вертикали
    elif (data [ROW1][COL_A ] == data [ROW2][COL_A ]) and (data [ROW1][COL_A ] == data [ROW3][COL_A ]) and (data [ROW1][COL_A ] != EMPTY):
        winner = data[ROW1][COL_A ]
    elif (data[ROW1][COL_B] == data[ROW2][COL_B]) and (data[ROW1][COL_B] == data[ROW3][COL_B]) and (data[ROW1][COL_B] != EMPTY):
        winner = data[ROW1][COL_B]
    elif (data[ROW1][COL_C] == data[ROW2][COL_C]) and (data[ROW1][COL_C] == data[ROW3][COL_C]) and (data[ROW1][COL_C] != EMPTY):
        winner = data[ROW1][COL_C]

     #  по диагонали
    elif (data [ROW1][COL_A ] == data [ROW2][COL_B]) and (data [ROW1][COL_A ] == data [ROW3][COL_C]) and (data [ROW1][COL_A ] != EMPTY):
        winner =data [ROW1][COL_A ]
    elif (data[ROW1][COL_C] == data[ROW2][COL_B]) and (data[ROW1][COL_C] == data[ROW3][COL_A ]) and (data[ROW1][COL_C] != EMPTY):
        winner = data[ROW1][COL_C]

# Победа Ничья если пустая клетка равна нулю
    elif emty_symbols == 0:
       winner = 'Ничья'

    return  winner



#функция для ввода значение Х и О
def input_value(input_value, value):
    column = input_value[1].lower() # колонки
    if column not in allowed_cols:   # если неправильная колонка
        print(f' [?] Вы ввели неверную колонку: {column}, ведите одну из правильных: {allowed_cols}, Ход потерян')
        return

    row = input_value[0]
    if row not in allowed_rows:   # если неправильная строка
        print(f' [?] Вы ввели неверную строку: {row}, ведите одну из правильных: {allowed_rows}, Ход потерян')
        return # ретурн позволяет дальше играть, невзирая на ошибку (4аx), просто пропуская ход

    # value = input_value[2].upper() # символ всегда будет с большой буквы
    # если наш value (буква) находиться в разрешенных символов  и символ не заполнен:
    #if (value in allowed_symbols) and (data[row][column] == EMPTY): можно ввести так
    if (value in allowed_symbols) and (data [row][column]  not in allowed_symbols):
       data [row][column] = value
    else:
        print(f' [?] Вы ввели неверный символ: {value}, ведите одну из правильных: {allowed_symbols}, '
              f'либо Вы ввели в ячейку которая занята, Ход потерян')
        return


#функция таблицы
 # данные 1а и пр. приобразуем в другой формат
def print_game_field():
      print('Данные вводятся в формате : 1a')
      print(f" \t a \t\t b \t\t c " )
      print('-' *25)
      print(f"1.\t {data[ROW1][COL_A ]} \t{data[ROW1][COL_B]} \t{data[ROW1][COL_C]} \n")
      print(f"2.\t {data[ROW2][COL_A ]} \t{data[ROW2][COL_B]} \t{data[ROW2][COL_C]} \n")
      print(f"3.\t {data[ROW3][COL_A ]} \t{data[ROW3][COL_B]} \t{data[ROW3][COL_C]} \n")


def run_game ():
    print('Игра __Крестики-Нолики__ Началась')
    print_game_field()
    # задаем каждому игрому ход, по очереди
    user = 'X'
    while game_end() == STATUS_CONTINUE:
     input_value(input(f'Ваш ход: ({user})' ), user)
     print_game_field()
     if user == 'X' :
         user = 'O'
     else:
         user = 'X'
     game_end() == STATUS_CONTINUE

     print(f'Игра закончилась! Победа за : {game_end()} ')


run_game()