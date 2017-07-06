
def get_number():
    return int(input("Please enter a number: "))

def not_prime():
    if number % i == 0:
        print("This is not prime number")

def is_prime():
    if number % i != 0:
        print("This is a prime number")

number = get_number()

for i in range(2, number):
   not_prime()
   is_prime()
   break
