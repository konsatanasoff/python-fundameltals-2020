import math

first_num = int(input())
second_num = int(input())


def factorial_division(first_num, second_num):
    return math.factorial(first_num) / math.factorial(second_num)


print(f"{factorial_division(first_num, second_num):.2f}")