# Task №4 do a refactoring using list comprehension, map, filter
import random

list_with_numbers = list(range(10))
new_list = []

for i in list_with_numbers:
    if not i%2:
        new_list.append(i+random.random())

print(new_list)

# list comprehension
new_list_comprehension = [i + random.random() for i in range(10) if not i % 2]
print(new_list_comprehension)

# map, filter
my_new_list = map(lambda y: y + random.random(), filter(lambda x: not x % 2, list(range(10))))
print(list(my_new_list))

