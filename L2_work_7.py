# Task №7. Write a decorator that modifies a function in such a way that the result of its execution is returned in json format
import json


def decorator_json(func):
    def wrapped(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapped

@decorator_json
def summa(x):
    """summa calculates the sum of numbers from 1 to x"""
    result = 0
    for i in range(1, x + 1):
        result += i
    return f'Sum of numbers from 1 to {x} = {result}'

print(summa(7))


