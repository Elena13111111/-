# деораторы - @property
# namespace -это пространство имен, кот.находиться в оперативной памяти выделенной под этот файл "10. Области видимости переменных"
# namespace явл-ся data_list
# есть Stuck - кусочек в оперативной памяти, вызывает функции
# f, d, age2,data_list -это уже не глобальные,а локальные переменные, а лежат они в Stuck.
#AGE = 18 --> это явл-ся глобальной переменной. Находиться в оперативной памяти.

AGE = 18

def f(data_list):
    for d in data_list:
        pass
    age2 = 20
#def f2()--> эта функция будет ложиться отдельным вызовом функции Stuck
def f2():
    x = 1

    f2()  # это 2-ой вызов

f()  # это 1-ый вызов
>>18
#=================================================
age = 18 #глобальная переменная выше

def f():
    age= 20 # локальная переменная ниже, потому ее надо делать глобальной
    print(age)
f()
print(age)
>>20
>>18
# =====================================
#  Если хотим видеть глобальную переменную в локальной. age = 18 ->def f(): age= 20
age = 18 #глобальная переменная

def f():
    global age
    age= 20 # локальная переменная
    print(age)

f()
print(age)
>>20
>>20
# # таким образом мы меням нашу глобальную переменную (age = 18) на новое значение (age= 20).
# # Т.е. локальную перем-ую сделали глобальной.
# ============================================
age = 18 #глобальная переменная

def f():
     age= 20 # локальная переменная
     def f2() :
        age = 32
        print(age)

     f2()
     print(age)

f()
print(age)

>>32
>>20
>>18
# # принтуем по порядку
# =====================
age = 18 #глобальная переменная

def f():
     # global age
     age= 20 # локальная переменная
     def f2() :
        global age
        age = 32
        print(age)

     f2()
     print(age)

f()
print(age)
>>32 f()
>>20 f2()
>>32 f()

# делаем глобальную переменную в своей области видимости. У нас есть 2 области видимости f() и f2().
# а - f(),
# б - f2(),
# в-  f().

# если global age находиться только в def f2()--> тогда age= 32 будет   "а" и "в".
# >>32 f()
# >>32 f2()
# >>32 f()
# если global age находиться только в def f()--> тогда age= 32 будет   "а" .
# >>32 f()
# >>20 f2()
# >>20 f()
# если global age находиться только в def f() и f2()--> тогда age= 32 будет в 3-х ответах
# >>32 f()
# >>32 f2()
# >>32 f()
# ===========================
# Залезаем на уровень вверх при помощи слова nonlocal. Лезем в предыдущую локальную переменную age= 20.
age = 18 #глобальная переменная

def f():
     age= 20 # локальная переменная, она переопределена как age = 32
     def f2() :
        nonlocal age
        age = 32
        print(age)

     f2()
     print(age)

f()
print(age)
>>32
>>32
>>18
# ==============================
# Идем по порядку видимости
age = 1 #глобальная переменная

def f1():
     age= 2 # локальная переменная
     def f2() :
         age = 3
         def f3():
             age = 4
             print(age)
         f3()
         print(age)

     f2()
     print(age)

f1()
print(age)

>>4
>>3
>>2
>>1
# =====================
age = 1 #глобальная переменная

def f1():
     age= 2 # локальная переменная
     def f2() :
         nonlocal age
         age = 3
         def f3():
             nonlocal age
             age = 4
             print(age)
         f3()
         print(age)

     f2()
     print(age)

f1()
print(age)

>4
>4
>4
>1