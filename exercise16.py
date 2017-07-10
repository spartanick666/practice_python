import random

def random_num():
    return random.randint(0, 100)

def random_low():
    return random.choice('abcdefghijklmnopqrstuvwxyz')

def random_cap():
    return random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def random_sym():
    return random.choice('~!@#$%^&*()_+[];,./{}:"<>?')

pwd_list = [(random_num(),random_sym(),random_cap(),random_num(),random_low())]

