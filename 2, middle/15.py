numbers = list(range(1, 100))
print(numbers)
numbers2 = list(filter(lambda number: number % 2 == 0, numbers))
numbers3 = list(filter(lambda number: number % 10 == 0, numbers2))
numbers4 = list(filter(lambda number: number % 5 == 0, numbers3))
numbers5 = list(filter(lambda number: number % 20 == 0, numbers4))
print()

numbers2 = list(filter(lambda number: number % 2 == 0, numbers))
numbers3 = list(filter(lambda number: number % 10 == 0, numbers))
numbers4 = list(filter(lambda number: number % 5 == 0, numbers))
numbers5 = list(filter(lambda number: number % 20 == 0, numbers))
print(numbers2)
print(numbers3)
print(numbers4)
print(numbers5)