list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for element in list_a:
    if element < 5:
        print(element)


list_b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_c = []
for x in list_b:
    if x < 5:
        list_c.append(x)
print(list_c)


