import random

def random_num():
    return random.randint(0, 100).__str__()

def random_low():
    return random.choice('abcdefghijklmnopqrstuvwxyz')

def random_cap():
    return random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def random_sym():
    return random.choice('~!@#$%^&*()_+[];,./{}:"<>?')

pwd_list = [random_num(), random_sym(), random_cap(), random_num(), random_low(), random_sym()]

def random_pwd():
    return ''.join(pwd_list)

user_input = input("Hello, would you like to generate a random password? please select yes or no: ").lower()

if user_input == "yes":
    print(random_pwd())
elif user_input == "no":
    print("Don't you want a password?")
else:
    print("Sorry I don't understand")