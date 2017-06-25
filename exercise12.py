import random

random_list = random.sample(range(100), 15)

def first_last():
    return(random_list[0], random_list[-1])

print("Your random list is: ", random_list)
print("\nThis first and last elements in the list are: ", first_last())

