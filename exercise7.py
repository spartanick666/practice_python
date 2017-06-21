a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_list = []

for x in a:
    if x % 2 == 0:
        even_list.append(x)
print(even_list)


even_list = [x % 2 == 0 for x in a]
print(even_list)