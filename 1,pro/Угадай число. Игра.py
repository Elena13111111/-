import random

# загадываем от 1 до 100
from_number = 1
to_number = 100
number = random.randint(from_number, to_number)
user1 = input('Ваше имя игрок1: ')
user2 = input('Ваше имя игрок2: ')
# пояснение что загаданное число от 1 до 100
print(f"Рыба карась, игра началась. [{from_number} - {to_number}]")

# ход для 1-го игрока
while True : # вечный цикл
  number1 = int(input(f'{user1} ваш ход: '))
  if number1 == number:
    print(f'{user1} ПОБЕДИЛ!!! УРАА!!!')
    break # данный цикл заканчивается
  elif number1 > number:
      print('Загаданное число меньше')
  else:
    print('Загаданное число больше')

# ход для 2-го игрока
  number2 = int(input(f'{user2} ваш ход: '))
  if number2 == number:
    print(f'{user2} ПОБЕДИЛ!!! УРАА!!!')
    break  # данный цикл заканчивается
  elif number2 > number:
    print('Загаданное число меньше')
  else:
    print('Загаданное число больше')