# Задание №2 Функция, число в степень
def new_power(x, y):
    return x ** y


print('Введите два целых числа через пробел ')
a, b = map(int, input().split())

power = new_power(a, b)
print(f'Число {a} в степени {b} = {power}')
