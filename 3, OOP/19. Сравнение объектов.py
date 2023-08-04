# Занятие 19. Сравнение объектов
# Сравнение объектов
# eq - равно
# lt - меньше
# le - меньше или равно
# qt - больше
# qe - больше или равно
# Инверсия

class Products:
    def __init__(self, products, bonuses=0 ): # бонусы по умолчанию =0
        self.bonuses = bonuses
        self.products = products #словарик продуктов будем задавать

    def get_products_price(self): #суммирование продуктов
        return sum(self.products.values()) - self.bonuses  #сумма-бонусы


    def __str__(self):
       return f'Цена: {self.get_products_price()}. {self.products}'  # сумма покупок

    #  метод для сравнения по сумме/эквивалент
    def __eq__(self, other):
        return self.get_products_price() == other.get_products_price()
    # #первый сумма продукта сравниваем с другими

    #  метод для сравнения по каждому объекту/эквивалент.
    # def __eq__(self, other):
    #     res = True # результат по умолчанию равно ИСТИНО
    #     #тогда сравниваем self с other

    #  метод для сравнения больше
    def __gt__(self, other):
        return self.get_products_price() > other.get_products_price()

    #  метод для сравнения больше или равно
    def __ge__(self, other):
        return self.get_products_price() >= other.get_products_price()

    #  метод для сравнения меньше
    # def __lt__(self, other):
    #     return self.get_products_price() < other.get_products_price()








products1 =Products({'молоко' :3, 'сыр':5}) #словарик покупок
products2 =Products({'мясо' :7})
products3 =Products({'молоко' :3, 'сыр':5})
# print( products1 == products3 ) #исп-ли __eq__ метод сравнение (по сумме)
#  >>True
# print(products1 == products2, products1, products2)
# >>False  Цена: 8. {'молоко': 3, 'сыр': 5} Цена: 9. {'мясо': 9} / 8 не равно 9. потому False
# print(products1 > products2,products1.get_products_price(), products2.get_products_price())
print(products1 > products2) #сокращенный вариант
#  >>True               8 7/ 8 больше 7
# print(products1 < products2,products1.get_products_price(), products2.get_products_price())
print(products1 <= products2)
# >>False         8 7 / 8 меньше 7
# print(products1 >=products3,products1.get_products_price(), products3.get_products_price())
print(products1 >=products3)
#  >>True     8 8
print(products1 !=products2) #не равно/ 8 не равно 7
#  >>True

# print(products1 != products2)  Если это выражение
# # products1 != products2
# # not (products1 == products2) то прога приобразцет ее так