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
