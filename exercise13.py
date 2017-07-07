#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
#Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of
#numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in
#the sequence is the sum of the previous two numbers in the sequence.
#The sequence looks like this: 1, 1, 2, 3, 5, 8, 13)

fib_num = int(input("How many Fibonnaci numbers should I generate? Please enter a number: "))
#fib_list = []

#for i in range(1, fib_num + 1):
 #   fib_list.append(i)
#print(fib_list)

def fib(n):
   if n == 1:
      return 1
   elif n == 0:
      return 0
   else:
    return fib(n-1) + fib(n-2)

for x in range(1, fib_num + 1):
    print(fib(x))