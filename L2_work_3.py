# Task №3 The function finds the factorial of a number
# cycle for
def fac_for(a):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


n = int(input('Enter the number '))

value = fac_for(n)
print(f'{n}! = {value}')


# cycle while
def fac_while(j):
    factorial = 1
    while j > 1:
        factorial *= j
        j -= 1
    return factorial


n = int(input('Enter the number '))

value = fac_while(n)
print(f'{n}! = {value}')


# recursion
def fac_recursion(x):
    if x > 1:
        return x * fac_recursion(x - 1)
    else:
        return 1


n = int(input('Enter the number '))

value = fac_recursion(n)
print(f'{n}! = {value}')
