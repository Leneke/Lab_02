# Задание №3 Функция, факториал числа
# цикл for
# def fac(a):
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial *= i
#     return factorial
#
#
# n = int(input('Введите число '))
#
# value = fac(n)
# print(f'{n}! = {value}')


# цикл while
# def fac(j):
#     factorial = 1
#     while j > 1:
#         factorial *= j
#         j -= 1
#     return factorial
#
#
# n = int(input('Введите число '))
#
# value = fac(n)
# print(f'{n}! = {value}')


# рекурсия
def fac(x):
    if x > 1:
        return x * fac(x - 1)
    else:
        return 1


n = int(input('Введите число '))

value = fac(n)
print(f'{n}! = {value}')
