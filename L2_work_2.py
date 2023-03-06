# Task №2 The function raises the number x to the power y of user enters numbers
def new_power(x, y):
    return x ** y


print('Enter two integers separated by a space ')
a, b = map(int, input().split())

power = new_power(a, b)
print(f'Number {a} to the power {b} = {power}')
