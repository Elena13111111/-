# Занятие 18. Складываем объекты класса
# - add
# - radd
# - ДЗ

# self: Ссылка на экземпляр.

# other: Объект, который следует вычесть из текущего.

# class Products:
#     def __init__(self, products):
#         self.products = products #словарик продуктов будем задавать
#
#     def get_products_price(self): #суммирование продуктов
#         return sum(self.products.values())
#
#     def __add__(self, other):  # для добавления новых покупок и их суммирование
#         new_products = {}  #делаем новый словарик
#         for product , price in self.products.items() : # проходим по словарику self
#             if product not in new_products:
#                 new_products[product] = price # словарик (1 продукт)= цене
#
#         for product, price in other.products.items():  #  для other
#                 if product not in new_products:
#                     new_products[product] = price
#         return Products(new_products)
#
#
# products1 =Products({'молоко' :3, 'сыр':5}) #словарик покупок
# # >> {'молоко': 3, 'сыр': 5}
# print(f'Цена: {products1.get_products_price()}. {products1.products}')   #сумма покупок
# # >>Цена: 8. {'молоко': 3, 'сыр': 5}
# products2 =Products({'кефир' :2, 'колбаса':10}) #добавляем словарик покупок
# products3 = products1 + products2
# print(f'Цена: {products3.get_products_price()}. {products3.products}')   #сумма покупок
# >>Цена: 20. {'молоко': 3, 'сыр': 5, 'кефир': 2, 'колбаса': 10}
# ==========================
# дополнение с примером/ бонусные баллы
class Products:
    def __init__(self, products, bonuses=0 ): # бонусы по умолчанию =0
        self.bonuses = bonuses
        self.products = products #словарик продуктов будем задавать

    def get_products_price(self): #суммирование продуктов
        return sum(self.products.values()) - self.bonuses  #сумма-бонусы

    def __add__(self, other):  # для добавления новых покупок и их суммирование
        # чтобы вписывать (int) Число
        if isinstance(other, int): #если наш  объект other и он явл-ся Число
            return Products(self.products, self.bonuses + other) #старые продукты и новые +бонусы
        elif isinstance(other, Products): # сверяем  на Products

          new_products = {}  #делаем новый словарик
          for product , price in self.products.items() : # проходим по словарику self
            if product not in new_products:
                new_products[product] = price # словарик (1 продукт)= цене

          for product, price in other.products.items():  #  для other
                if product not in new_products:
                    new_products[product] = price
          return Products(new_products)

    # эта функция для перевернутого значения
    def __radd__(self, other): # если 5 + products3 , поставим впереди (сумм мест слагаемых)
        if isinstance(other, int):
            return Products(self.products, self.bonuses + other)


products1 =Products({'молоко' :3, 'сыр':5}) #словарик покупок
# >> {'молоко': 3, 'сыр': 5}
print(f'Цена: {products1.get_products_price()}. {products1.products}')   #сумма покупок
# >>Цена: 8. {'молоко': 3, 'сыр': 5}
products2 =Products({'кефир' :2, 'колбаса':10}) #добавляем словарик покупок
products3 = products1 + products2
print(f'Цена: {products3.get_products_price()}. {products3.products}')   #сумма покупок
# >>Цена: 20. {'молоко': 3, 'сыр': 5, 'кефир': 2, 'колбаса': 10}
products4= products3 + 5  #отнимаем  5 бонусов
print(f'Цена: {products4.get_products_price()}.{products4.products}')
# >>Цена: 15.{'молоко': 3, 'сыр': 5, 'кефир': 2, 'колбаса': 10}
products5 = 1 + products4
print(f'Цена: {products5.get_products_price()}.{products5.products}')
# >>Цена: 14.{'молоко': 3, 'сыр': 5, 'кефир': 2, 'колбаса': 10}
