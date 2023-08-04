# Занятие 11. Замыкания
# - Пример счётчика
# - Замыкания

- Замыкания
def get_medical_service(preparat):
    def do_treat(): #ссылается на внешнюю видимость preparat
        print(f'[{preparat}]Я вылечелил тебя')
    return do_treat

treater1 = get_medical_service('Парацетамол') # явл-ся функцией do_treat
treater2 = get_medical_service('Укол')

treater1()
treater1()
treater2()
treater2()
treater2()
treater2()
[Парацетамол]Я вылечелил тебя
[Парацетамол]Я вылечелил тебя
[Укол]Я вылечелил тебя
[Укол]Я вылечелил тебя
[Укол]Я вылечелил тебя
[Укол]Я вылечелил тебя
# ===============================
#Счетчик
def init_counter(start_from=0):
    def count():
        nonlocal start_from # nonlocal мопомогает взять верхнюю переменую start_from
        start_from +=1
        print(f'Номер: {start_from}')
    return count # возвращает ссылку , а не функцию.


counter1 = init_counter(0) # счетчик от 1 до 5
counter2 = init_counter(100)# счетчик от 101 до 109
counter1()
counter1()
counter1()
counter1()
counter1()
counter2()
counter2()
counter2()
counter2()
counter2()
counter2()
counter2()
counter2()
counter2()

Номер: 1
Номер: 2
Номер: 3
Номер: 4
Номер: 5
Номер: 101
Номер: 102
Номер: 103
Номер: 104
Номер: 105
Номер: 106
Номер: 107
Номер: 108
Номер: 109


