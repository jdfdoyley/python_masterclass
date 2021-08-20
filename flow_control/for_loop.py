# pylint: disable=C0103
"""In this file I will demonstrate the use of Python for Loop."""

# PYTHON FOR LOOP
# The for statement in Python is a bit different from what you usually use in
# other programming languages.

# Rather than iterating over a number progression, Python's for statement
# iterates over the items of any iterable (list, tuple, dictionary, set, or
# string). The items are iterated in the order that they appear in the iterable.

# SYNTAX
# for var in iterable:
#     statement
#     statement
#     ...
# else:
#     statement
#     statement
#     ...

# BASIC EXAMPLES

# Iterate through a list
dogs = ['german shepherd', 'poodle',
        'pomeranian', 'bulldog', 'chihuahua', 'pug']
for dog in dogs:
    print(dog.title())

print()

# Iterate through a string
dog = 'pomeranian'
for letter in dog:
    print(letter)

print()

# BREAK IN FOR LOOP
# Python break statement is used to exit the loop immediately. It simply jumps
# out of the loop altogether, and the program continues after the loop.

# Break the loop at 'bulldog'
dogs = ['german shepherd', 'poodle',
        'pomeranian', 'bulldog', 'chihuahua', 'pug']
for dog in dogs:
    if dog == 'bulldog':
        break
    print(dog.title())

print()

# CONTINUE IN FOR LOOP
# The continue statem skips the current iteration of a loop and continues with
# the next iteration.
dogs = ['german shepherd', 'poodle',
        'pomeranian', 'bulldog', 'chihuahua', 'pug']
for dog in dogs:
    if dog == 'bulldog':
        continue
    print(dog.title())

print()

# ELSE IN FOR LOOP
# Python allows an optional else clause at the end of a for loop. The else
# clause will be executed if the loop terminates naturally (through exhaustion)
dogs = ['german shepherd', 'poodle',
        'pomeranian', 'bulldog', 'chihuahua', 'pug']
for dog in dogs:
    print(dog.title())
else:
    print('All items have been printed!')

print()

# If the loop gets terminated prematurely with break, the else cluase will be
# skipped.
dogs = ['german shepherd', 'poodle',
        'pomeranian', 'bulldog', 'chihuahua', 'pug']
for dog in dogs:
    if dog == 'chihuahua':
        break
    print(dog.title())
else:
    print('All items have been printed!')

print('I appear after the else block!')

print()

# RANGE() FUNCTION IN FOR LOOP
# If you need to execute a group of statements for specified number of times,
# use built-in function range()

# The range(start, stop, step) function generates a sequence of numbers from 0
# up to (but not including) the specified number

# Generate a sequence of numbers from 0 - 6
for num in range(7):
    print(num)

# range() provides a simple way to repeat an action a specific number of times.

print()

# Print 'Hello!' three times
for x in range(3):
    print('Hello!')

print()

# The range starts from 0 by default. But, you can start the range at another
# number by specifying the start parameter.

# Generate a sequence of numbers from 2 to 6
for x in range(2, 7):
    print(x)

print()

# You can generate a range of negative numbers as well.
for x in range(-5, 0):
    print(x)

print()

# The range increments by 1 by default. But, you can specify a different
# increment by adding a step parameter.

# Incrememnt the range with 2
for x in range(2, 7, 2):
    print(x)

print()

# NESTED FOR LOOP
# A loop inside another loop is called a nested loop.

# Flatten a nested list
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for items in numbers:
    for item in items:
        print(item)

print()

# ACCESS INDEX IN FOR LOOP
# To iterate over the indices of a sequence, you can combine range() and len()
# as follows:
dogs = ['german shepherd', 'poodle',
        'pomeranian', 'bulldog', 'chihuahua', 'pug']
for index in range(len(dogs)):
    print(index, dogs[index])

print()

dogs = ['german shepherd', 'poodle',
        'pomeranian', 'bulldog', 'chihuahua', 'pug']
for index, value in enumerate(dogs):
    print(index, value)

print()

# UNPACKING IN A FOR LOOP
# Below for loop does a multiple assignment (unpack the current tuple) each
# time through the loop.

# Tuple unpacking
tuple_list = [
    (1, 2),
    (3, 4),
    (5, 6)
]
for (a, b) in tuple_list:
    print(a, b)

print()

# Likewise, you can iterate through both keys and values in a dictionary.

# Dictionary unpacking
dict_list = {'name': 'Bob', 'age': 25}
for x, y in dict_list.items():
    print(x, y)

print()

# MODIFY A LIST WHILE ITERATING
# Don't alter mutable objects while looping on them. It may create a infinite
# loop.

# infinite loop
# colors = ['red', 'green', 'blue']
# for x in colors:
#     if x == 'red':
#         colors.insert(0, 'orange')
#         print(colors)

# It is recommended that you first make a copy. The slicing operator makes this
# especially convenient.
colors = ['red', 'green', 'blue', 'red']
for x in colors[:]:
    if x == 'red':
        colors.insert(0, 'orange')
print(colors)

print()

# LOOPING THROUGH MULTIPLE LISTS
# Using built-in zip() function you can loop through multiple lists at once.

# Loop through two lists at once
name = ['Cameron', 'Jody', 'Sasha']
age = [25, 26, 27]
for x, y in zip(name, age):
    print(x, y)
