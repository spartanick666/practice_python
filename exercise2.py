number = int(input("Please input a number: "))

if number % 4 == 0:
    print("Your number is divisible by 4." )
elif number % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")

num = int(input("Please input your first number: "))
check = int(input("Please input your second number: "))

if num % check == 0:
    print(check, "divides evenly into", num)
else:
    print(check, "does not divide evenly into", num)