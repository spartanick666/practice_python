import random


my_random3 = []

# generate a list of 99 random numbers
my_random1 = random.sample(range(100), 99)
# generate a list of 15 random numbers
my_random2 = random.sample(range(100), 15)

# print list to verify lists created
print(my_random1)
print(my_random2)

# loop numbers in list1 and if any are the same in list 2, append to new new list
for x in my_random1:
    for y in my_random2:
        if x == y:
            my_random3.append(y)

c = set(my_random3)
print("\nThe following numbers are contained in both random lists:\n", my_random3)
