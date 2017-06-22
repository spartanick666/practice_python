import random

a = random.sample(range(100), 25)
b = random.sample(range(100), 15)

print(a)
print(b)
list = []

for x in a:
    for y in b:
        if x == y:
            list.append(y)

print("\nThe following numbers are contained in both lists:", list)

