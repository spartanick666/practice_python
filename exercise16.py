# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
# lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password
# every time the user asks for a new password. Include your run-time code in a main method.

import random

def ask_question():
    return input("Hello, would you like to generate a strong random password? please select yes or no: ").lower()

def random_num():
    return random.randint(0, 100).__str__()

def random_low():
    return random.choice('abcdefghijklmnopqrstuvwxyz')

def random_cap():
    return random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def random_sym():
    return random.choice('~!@#$%^&*()_+[];,./{}:"<>?')

def weak_pwd():
    weak_list = ['love', '12345', 'password', 'guest', 'qwerty', 'root']
    return ("Here is your weak password: " + random.choice(weak_list))

pwd_list = [random_num(), random_sym(), random_cap(), random_low(), random_sym(), random_low(), random_cap()]

def random_pwd():
    return ''.join(pwd_list)

if __name__ == '__main__':
    user_input = ask_question()
    if user_input == "yes":
        print(random_pwd())
    elif user_input == "no":
        print(weak_pwd())
    else:
        print("Sorry I don't understand")