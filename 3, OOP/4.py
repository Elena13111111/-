# a, b, c = 'альфа', 'бетта', 'гамма'
# print(a) # переменная а: альфа принадлежит первой [0]
# print(b) # переменная b: бетта принадлежит второй [1]
# print(c) # переменная c: гамма принадлежит третьей [2]
# print(b)

# 1
# a, *b, c = ['a', 'b', 1, 2, 3, 4, 5]
# print(a)
# print(b)
# print(c)

# 2 список значений
# nums = [5, 10]
# print(list(range(10)))
# print(list(range(5, 10)))
# print(list(range(*nums)))

# *a, b, c = 'альфа', 'бетта', 1, 2 ,5
# print(a)
# print(b)
# print(c)

# 3
# print(1, 2, 3)
# print(*[1, 2, 3])
# a, b, c = [1, 2, 3]
# print(a, b, c)

# 4
# def ab(a, b):
#     print(a, b)
# elems = ['a', 'b']
# ab('a', 'b')
# ab(*elems)
# ab(*['a', 'b'])
# ab('a', 'b')
# print(*nums)

# 5
# def super_sum1(numbers):
#     res = 0
#     for number in numbers:
#         res += number
#         print(f'Сумма = {res}')
# super_sum1([1, 2, 3, 4, 5])
# print('=' * 80)
# def super_sum2(*numbers):
#     res = 0
#     for number in numbers:
#         res += number
#         print(f'Сумма = {res}')
# super_sum2(1, 2, 3, 4, 5)

# 6
# print(1, 2, 3, 4)
# print(1, 2, 3, 4, sep='=)')
# print(1, 2, 3, 4, sep='\n')

# 7
# def func(arg1, arg2,arg3, *args, **kwargs):
#     print(arg3)
#     print(arg1)
#     print(arg2)
#
#     print(args)
#     print(kwargs)
# func(
#     1, 2, 'a', 'b', 'EEEEEEE', [1, 2, 3],
#     key1='123', key2='abc', key3='123'
# )

