print('Hello Wolrd')

print("Hello World")

print('Hello Valerie!')

print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

print('She said: "Hello" and then left.')

print("A 'single quote' inside a double quote")
print('A "double quote" inside a single quote')
print("Alternatively you can just \"escape\" the quote")

print('Hello world!\nHello world!')

print('Hello' + " " + 'Valerie')

# Fix the code below 👇

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")
    

print("What is your name?")

print("Hello " + input("What is your name?"))

# making notes

#❌
print(input("What is your name?"))
#✅
print(input())

#✅
num1 = int(input())
num2 = int(input())

print(num1 * num2)

#❌
num1 = int(input())
num2 = int(input())

print(6)

# using len
numOfLetters = len("Angela")
print(numOfLetters)

# Write a program that calculates and outputs the number of characters in any name. The automated tests will try out lots of different names as the input. Your code should work for any name. Your code should only output the number, no other text is needed.
# Hint
# Remember, you can use len() around any piece of text to calculate the number of characters.
# e.g. https://www.google.com/search?q=how+to+get+the+length+of+a+string+in+python+stack+overflow
# Important
# Don't add prompt text to the input() function.
# e.g. use
# ✅ name = input()
# don't use:
# ❌ name = input("What's your name?")

num_of_letters = len(input())
print(num_of_letters)

