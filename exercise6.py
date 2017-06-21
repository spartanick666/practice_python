word = input("Please Enter a single word or string: ")
reversed_word = word[::-1]

if list(word) == list(reversed_word):
   print("This is a palindrome")
else:
   print("This is not palindrome")