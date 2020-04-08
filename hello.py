# Python Basics:

# print("Hello, World!")

# Create a prompt
# answer = input("What's your name?\n")
# print(f"Hello, {answer}")
# # Or the same result
# print("Hello,", answer)

# Get an int input and do some math ####
# age = int(input("What's your age?\n"))
# print(f"You are at least {age * 365} days old")

# # Set a variable
# counter = 1
# counter += 1
# print(counter)

# Basic conditionals:
# x = int(input("x: "))
# y = int(input("y: "))
# # If statements:
# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x is equal to y")

# Prompt user to agree #####
# s = input("Do you agree?\n")

# Check whether agree
# if s == 'Y' or s == 'y':
# if s.lower() in ['y', 'yes']:
#     print("Agreed.")
#  elif s == 'N' or s == 'n':
# elif s.lower() in ['n', 'no']:
#     print("Not agreed.")
# While statements:
# Boolean values in Python must be Capitalized
# while True:
#     print("Hello, world!")        ## Infinite loop

# i = 3
# while i > 0:
#     print("cough")
#     i -= 1

# For loop statements:

# for i in [0, 1, 2]:
#     print("cough")

# Better way
# for i in range(3):
#     print("cough")

# Date types ###########
# - bool ## the True and False first letter capitalized
# - float
# - int
# - str

# - range  ## sequence of numbers
# - list   ## sequence of mutable values/it's like an array auto size
# - tuple  ## sequence of immutable values
# - dict   ## collection of key/value pairs /Underneath the hood they are hash tables
# - set    ## collection of unique values

# Overwriting the print function arguments

# for i in range(4):
#     # print("?", end="")   # When you like to print something horizontally
#     print("?", end=",")
# print()   # Gives us a new line

# Pythonic way
# print("?" * 4)

# Nested Loop
# for i in range(3):
#     for j in range(3):
#         print('#', end="")
#     print()


# List
# Getting the average of some scores
# scores = [72, 73, 33]
#
# print(f"Average: {sum(scores) / len(scores)}")

# List examples:
# nums = [x for x in range(500)]   # Generates a list of num from 0 to 499
# print(nums)

##
# nums = [1, 2, 3, 4]
# # These 3 operations bellow do the same
# nums.append(5)
# nums.insert(5, 6)
# nums[len(nums):] = [7]
# print(nums)


# Iterating over strings and printing the letters horizontally
# s = input("Input: ")
# print(f"Output: ", end="")
# for c in s:
#     print(c, end="")
# print()

# Iterating over a string input and capitalized the letters
# s = input("Input: ")
# print("Output: ", end="")
# print(s.upper())
# # for c in s:
# #     print(c.capitalize(), end="")
# # print()

# Comparing two strings

# s = input("s: ")
# t = input("t: ")
#
# if s == t:
#     print("Same")
# else:
#  print("Different")

# Tuples #################### Ordered, immutable set of data
# Example of a List of Tuples
# presidents = [
#     ("George Washington", 1789),
#     ("John Adams", 1797),
#     ("Thomas Jefferson", 1801),
#     ("James Madison", 1809)
# ]
# print(presidents)
# for prez, year in presidents:
#     # print(f"In {year}, {prez} took office")  # Same bellow
#     print("In {1}, {0} took office".format(prez, year))
# print(presidents)

# Dictionaries: ################# collection of key/value pairs /Underneath the hood they are hash tables

pizzas = {
    "cheese": 9,
    "pepperoni": 10,
    "vegetables": 11,
    "buffalo chicken": 12
}

# pizzas["cheese"] = 8
#
# if pizzas["vegetables"] < 12:
#     # do something
#     print("To expensive!")
#
# pizzas["bacon"] = 14
#
# print(pizzas)

# for pie in pizzas:
#     # use pie in here as a stand-in for "i"
#     print(pie)

# for pie, price in pizzas.items():  # this .items() allow us to convert the dict into a list
#     print(price)

# for pie, price in pizzas.items():
#     print("A whole {} pizza costs ${}".format(pie, price))
#     print("A whole " + pie + " pizza cost $" + str(price))   # Same



