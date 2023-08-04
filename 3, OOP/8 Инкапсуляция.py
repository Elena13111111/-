class Point:
    MIN = -100
    MAX = 100
    DEFAULT_VALUE = 0

# этот метод дает меньше доступа
    @classmethod
    def __correct_value(cls, value):
        return value if cls.MIN <= value <= cls.MAX else cls.DEFAULT_VALUE

    # def __correct_value(self, value): # делаем приватным
    #     # если диапазон попадает между min и max тогда возвращаем value, если нет --> возращаем 0
    #       return value if self.MIN <= value <= self.MAX else self.DEFAULT_VALUE

    def __init__(self, x, y):
        self.__x = self.__correct_value(x)
        self.__y = self.__correct_value(y)


    def set_x(self, x): #поставляют данные
       self.__x = self.__correct_value(x)

    def set_y(self, y): #поставляют данные
       self.__y = self.__correct_value(y)

    def get_x(self): #получают данные. Они будут приватные, кот. трогать нельзя
        return self.__x

    def get_y(self): #получают данные. Они будут приватные, кот. трогать нельзя
        return self.__y


# point1 = Point(20, 90)
# # print(dir(point1))
#
# print(point1._Point__x, point1._Point__y )
# point1._Point__x = 1000
# point1._Point__y = 2000
# print(point1._Point__x, point1._Point__y )

point1 = Point(20, 90)
print(point1.get_x(), point1.get_y())
point1.set_x(101)
point1.set_y(50)
print(point1.get_x(), point1.get_y())