#Create a program that will play the “cows and bulls” game with the user. The game works like this: Randomly generate a
#4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct
#place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user
#makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is
#over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

import random

def compare_nums(rand_num, user_num):
    cowbulls = [0, 0]
    for i in range(len(user_num)):
        if user_num[i] == rand_num[i]:
            cowbulls[0]+=1
        else:
            cowbulls[1]+=1
    return cowbulls

playgame = True
rand_num = str(random.randint(0000,9999))
print(rand_num)

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playgame:
    user_num = input("Please select a 4 digit number: ")
    cbcount = compare_nums(rand_num, user_num)

    print("You have " + str(cbcount[0]) + " cows, and " + str(cbcount[1]) + " bulls.")

    if cbcount[0] == 4:
        print("Congrats, you got the correct number " + rand_num)
        break

    else:
        print("I didn't quite get that. Please select a 4 digit number again")

