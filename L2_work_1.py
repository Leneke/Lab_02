# Задание 1. Ошибки

# SyntaxError
# a = 'Hello world!
#
# IndentationError
# for i in range(3):
# print('Hello world!')

# NameError
# x = 0
# print(x + y)

# IndexError
# a = [1, 2, 3, 4]
# print(a[5])

# KeyError
# fruits = {'apple': 3, 'banana': 5, 'peach': 6}
# print(fruits['orange'])

# ImportError
# from random import raandint

# AttributeError
# a = 5
# print(a.capitalize())

# ZeroDivisionError
# x = 4
# y = 0
# c = x / y

# RuntimeError не получается, смогла сделать RecursionError это подкласс RuntimeError
# def factorial(x):
#     n = 0
#     if n == 0:
#         return n * factorial(n)
#
#
# print(factorial(5))