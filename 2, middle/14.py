
import traceback

numbers = [1, 2, 3]


def get_from_number(index):
    try:
        return numbers[index]
    except Exception as e:
        return 0


print(get_from_number(1))
print(get_from_number(2))
print(get_from_number(3))
print(get_from_number(4))