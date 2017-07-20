#Create a program that will play the “cows and bulls” game with the user. The game works like this: Randomly generate a
#4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct
#place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user
#makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is
#over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

import random

rand_num = str(random.randint(1000, 9999))

rand_list = []

for x in rand_num:
    rand_list.append(x)
print(rand_list)

number = input("Welcome to the Cows and Bulls game, Please enter in a 4 digit number: ")

num_list = []
for x in number:
    num_list.append(x)
print(num_list)
