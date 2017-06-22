import random

guess = int(input("Guess a number between 1 and 9: "))

random_num = random.randint(1, 9)

if guess == random_num:
    print("You guessed correctly")
elif guess > random_num:
    print("You guessed too high")
elif guess < random_num:
    print("You guessed too low")

print("The random number was", random_num)
