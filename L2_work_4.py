# Задание №4 использовать list comprehension
# было
# import random
# list_with_numbers = list(range(10))
# new_list = []
#
# for i in list_with_numbers:
#     if not i%2:
#         new_list.append(i+random.random())
#
# print(new_list)

# стало с list comprehension
import random

list_with_numbers = list(range(10))
new_list = [i + random.random() for i in list_with_numbers if not i % 2]
print(new_list)
