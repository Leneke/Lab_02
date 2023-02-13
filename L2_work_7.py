# Задание 7 написать декоратор
import json


def decorator_json(func):
    def wrapped(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapped

@decorator_json
def summa(x):
    """summa вычисляет сумму чисел от 1 до x"""
    result = 0
    for i in range(1, x + 1):
        result += i
    return f'Сумма чисел от 1 до {x} = {result}'

print(summa(7))
