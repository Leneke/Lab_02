# Задание №6 Сортировка словарей и списков
my_list = [(1, 1, 1), (1, 2, 3), (-1, -1, 7), (-3, 2, 8), (0, 0, 0), (3, -4, -5)]

# сортировка по сумме кортежей
my_list.sort(key=lambda i: sum(i))
print(my_list)

# сортировка по 3-му элементу
my_list.sort(key=lambda i: i[2])
print(my_list)


my_dict = {'b': 3, 'c': 2, 'a': 4, 'd': 1}

# сортировка ключей по алфавиту
print(sorted(my_dict.keys()))

# ключи в порядке убывания по значениям
new_dict = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print(new_dict.keys())

