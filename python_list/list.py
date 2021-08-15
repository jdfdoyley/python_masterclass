"""This file is responsible for demonstrating the use of List."""

# CREATE A LIST
# There are several ways to create a new list; the simplest is to enclose the
# values in square brackets []

# A list of integers
int_list = [1, 2, 3]

# A list of strings
ants = ['carpenter', 'fire', 'pharaoh', 'tapinoma']

# The items of a list don't have to be the same type. The following list
# contains an integer, a string, a float, a complex number, and a boolean

# A list of mixed datatypes
mixed_list = [1, 'abc', 1.23, (3+4j), True]

# A list containing zero items is called an empty list and you can create one with empty brackets []

# An empty list
empty_list = []

# THIS list() CONSTRUCTOR
# You can convert other data types to lists using Python's list() constructor.

# Convert a string to a list
str_list = list('abcdef')
print(str_list)

# Converting a tuple to a list
tup_list = list((1, 2, 3, 4, 5))
print(tup_list)

# NESTED LIST
# A list can contain sublists, which in turn can contain sublists themselves,
# and so on. This is known as nested list.

# You can use the to arrange data into hierarchical structures.
nested_list = [
    'a',
    [
        'bb',
        [
            'ccc',
            'ddd'
        ],
        'ee',
        'ff'
    ],
    'g',
    'h'
]

# ACCESS LIST ITEMS BY INDEX
# You can think of a list as a relationship between indexes and values.
# This relationship is called a mapping; each index maps to one of the values.

# Note that the first element of a list always at index zero.

# You can access individual items in a list using an index in square brackets
colors = ['red', 'green', 'blue', 'yellow', 'black']

# first item
print(colors[0])

# third item
print(colors[2])

# Python will raise an IndexError error, if you use an index that exceeds the
# number of items in your list.
print(colors[10])       # IndexError: list index out of range
