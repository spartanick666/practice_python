a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 99, 7, 22, 15]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 99]
c = []


for x in a:
    for y in b:
        if x == y:
            c.append(y)
c = set(c)
print(c)