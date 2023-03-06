# Task №6 Sorting dictionaries and lists
my_list = [(1, 1, 1), (1, 2, 3), (-1, -1, 7), (-3, 2, 8), (0, 0, 0), (3, -4, -5)]

# sort by sum of tuples
my_list.sort(key=lambda i: sum(i))
print(my_list)

# sort by 3rd element
my_list.sort(key=lambda i: i[2])
print(my_list)


my_dict = {'b': 3, 'c': 2, 'a': 4, 'd': 1}

# sort keys alphabetically
print(sorted(my_dict.keys()))

# keys in descending order by value
new_dict = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print(new_dict.keys())

