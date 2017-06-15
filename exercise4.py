number = int(input("Hello, please input a number: "))
num_range = range(1, number + 1)

list1 = []

for x in num_range:
    if number % x == 0:
        list1.append(x)
print(list1)