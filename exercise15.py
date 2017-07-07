#Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.

#don't call funtion string/ make unique
def string():
    return (input("Please input a string: "))

def split_string():
    return string().split()

print(reversed(split_string()))


