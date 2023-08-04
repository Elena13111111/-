# Домашка 2
# Реализовать методы __sub__ и __rsub__ :
# 1. Для удаления одного набора продуктов из другого набора продуктов
# 2. Реализовать удаление бонусных балов (Products - целое число)

# x - y
# __sub__(self, other)
#
# x - y
# object.__rsub__(self, other)



# class NumOperations(object):
#     def __init__(self, math_list):
#         self.math_list = math_list
#     def __sub__(self, other):
#         minuslst = []
#         zipped = zip(self.math_list, other.math_list)
#         for tup in zipped:
#             minuslst.append(tup[0] - tup[1])
#         return NumOperations(minuslst)
#
#     def __add__(self, other):
#         addlst = [x + y for x, y in zip(self.math_list, other.math_list)]
#         return NumOperations(addlst)
#     def __mul__(self, other):
#         mullst = [x * y for x, y in zip(self.math_list, other.math_list)]
#         return NumOperations(mullst)
#     def __repr__(self):
#         return str(self.math_list)
# x = NumOperations([100, 90, 80, 70, 60])
# y = NumOperations([10, 9, 8, 7, 6])
# p = x - y
# z = x + y
# q = x * y
#
# print('Вычитание: ' + str(p))
# print('Прибавление: ' + str(z))
# print('Умножение: ' + str(q))
#
#
# >>Деление: [90, 81, 72, 63, 54]
# >>Прибавление: [110, 99, 88, 77, 66]
# >>Умножение: [1000, 810, 640, 490, 360]
# ==============================
# Класс, описывающий точку на координатной плоскости
# class Point:
#
#     # Конструктор класса
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         return
#
#     # Методы доступа к полям self.x, self.y
#     def GetX(): return self.x
#     def GetY(): return self.y
#     def SetXY(self, x, y):
#         self.x = x
#         self.y = y
#         return
#
#     #-------------- Методы перегрузки операторов --------------
#     # Перегрузка бинарного оператора + (суммирование объектов) - метод __add__()
#     def __add__(self, pt):
#         obj = Point(self.x + pt.x, self.y + pt.y)
#         return obj
#
#     # Перегрузка бинарного оператора вычитания - метод __sub__()
#     def __sub__(self, pt):
#         # вычитание координат
#         obj = Point(self.x - pt.x, self.y - pt.y)
#         return obj
#
#     # ---------------------------------------------------------
#     # Метод, который выводит значения внутренних координат x, y
#     def Print(self, msg):
#         print(msg, " => x = ", self.x, "; y = ", self.y)
#         return
#
# # Тестирование
# pt1 = Point(1,3)
# pt1.Print("pt1")
#
# pt2 = Point(2,6)
# pt2.Print("pt2")
#
# pt3 = pt1 + pt2
# pt3.Print("pt1 + pt2")
#
# (pt1-pt2).Print("pt1 - pt2")

# pt1  => x =  1 ; y =  3
# pt2  => x =  2 ; y =  6
# pt1 + pt2  => x =  3 ; y =  9
# pt1 - pt2  => x =  -1 ; y =  -3
# --------------------------------

# Products={
#     'молоко' :3,
#     'сыр':5,
#     'рыба': 15,
#     'Манго':13
# }
# print(Products)
# del Products['сыр']
# print(Products)
# -------------------------------

# Домашка 2
# Реализовать методы __sub__ и __rsub__ :
# 1. Для удаления одного набора продуктов из другого набора продуктов
# 2. Реализовать удаление бонусных балов (Products - целое число)

# x - y
# __sub__(self, other)
#
# x - y
# object.__rsub__(self, other)



class Products:
    def __init__(self, products, bonuses=0 ): # бонусы по умолчанию =0
        self.bonuses = bonuses
        self.products = products #словарик продуктов будем задавать

    def get_products_price(self): #суммирование продуктов
        return sum(self.products.values()) - self.bonuses  # суммирование
         # sum(self.products.values)) +self.bonuses
        if isinstance(other, Products):  # если нам пришел экземпляр Product, у other будет и словарь products,  и бонусы
             new_bonus = self.bonus - other.bonus
        return sum(self.products.values()) - new_bonus



     # для убавления  покупок и их суммирование
    def __add__(self, other):  # для добавления новых покупок и их суммирование
        # чтобы вписывать (int) Число
        if isinstance(other, int):  # если наш  объект other и он явл-ся Число
            return Products(self.products, self.bonuses + other)  # старые продукты и новые +бонусы
        elif isinstance(other, Products):  # сверяем  на Products
            # new_bonus = self.bonus - other.bonus  # бонусы
            new_products = {}  # делаем новый словарик
            for product, price in self.products.items():  # проходим по словарику self
                if product not in new_products:
                    new_products[product] = price  # словарик (1 продукт)= цене

            for product, price in other.products.items():  # для other
                if product not in new_products:
                    new_products[product] = price
            return Products(new_products)

            # эта функция для перевернутого значения
    def __radd__(self, other): # если 5 + products3 , поставим впереди (сумм мест слагаемых)
        if isinstance(other, int):
            return Products(self.products, self.bonuses + other)
# данные о бонусах
    def __sub__(self, other):
        if isinstance(other, int):
            return Products(self.products, self.bonuses - other)
        elif isinstance(other, str):
            new_products = {}
            for name, price in self.products.items():
                if name != other:
                    new_products[name] = price
            return Products(new_products, self.bonuses)
        elif isinstance(other, Products):
            new_bonus = self.bonus - other.bonuses
            return sum(self.products.values()) - new_bonus

    def __rsub__(self, other):
        if isinstance(other, int):
            return Products(self.products, self.bonuses - other)



products1 =Products({'молоко' :3, 'сыр':5, 'рыба': 15, 'Манго':13}) #словарик покупок

print(f'Цена : {products1.get_products_price()}. {products1.products}')   #сумма покупок
# >>Цена: 36. {'молоко': 3, 'сыр': 5, 'рыба': 15, 'Манго': 13}
products4 =Products({'кефир' :2, 'колбаса':10})
products5= products1 + products4
print(f'Цена : {products5.get_products_price()}. {products5.products}  добавляем 2 продукта. Вывод:',products5.bonuses, 'балла')
#>>Цена : 43. {'молоко': 3, 'рыба': 15, 'Манго': 13, 'кефир': 2, 'колбаса': 10}  добавляем 2 продукта. Вывод: 0 балла
products6 =products5 - 'колбаса'
products7 = products6 - 'кефир'
print(f'Цена : {products7.get_products_price()}. {products7.products} .Убрали 2 продукта Вывод:',products7.bonuses, 'балла')
#>>Цена : 43. {'молоко': 3, 'рыба': 15, 'Манго': 13, 'кефир': 2, 'колбаса': 10}  добавляем 2 продукта. Вывод: 0 балла
products8 = products7 +10
print(f'Цена : {products8.get_products_price()}. {products8.products} + 10 баллa. Вывод:',products8.bonuses, 'балла')
#>>Цена : 26. {'молоко': 3, 'сыр': 5, 'рыба': 15, 'Манго': 13} + 10 баллa. Вывод: 10 балла
products9 = products8 +5
print(f'Цена : {products9.get_products_price()}. {products9.products} + 5 баллa. Вывод:',products9.bonuses, 'балла')
#>>Цена : 21. {'молоко': 3, 'сыр': 5, 'рыба': 15, 'Манго': 13} + 5 баллa. Вывод: 15 балла
products10 = products9 -4
print(f'Цена : {products10.get_products_price()}. {products10.products} удаляем 4 баллa. Вывод:',products10.bonuses, 'балла')
#>>Цена : 25. {'молоко': 3, 'сыр': 5, 'рыба': 15, 'Манго': 13} даляем 4 баллa. Вывод: 11 балла
products11 =6- products10
print(f'Цена : {products11.get_products_price()}. {products11.products} удаляем 6 баллa. Вывод:',products11.bonuses, 'балла')
#>>Цена : 31. {'молоко': 3, 'сыр': 5, 'рыба': 15, 'Манго': 13} удаляем 6 баллa. Вывод: 5 балла


