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
# print(colors[10])       # IndexError: list index out of range

# NEGATIVE LIST INDEXING
# You can access a list by negative indexing as well. Negative indexes count
# backward from the end of the list. So L[-1] refers to the last item, L[-2] is
# the second-last, and so on.

colors = ['red', 'green', 'blue', 'yellow', 'black']

print(colors[-1])       # black

print(colors[-2])       # yellow

# ACCESS NESTED LIST ITEMS
# You can access individual items in a nested list using multiple indexes. The
# first index determines which list to use, and the second indicates the value
# within that list.

nested_list = [
    'a',
    'b',
    [
        'cc',
        'dd',
        [
            'eee',
            'fff'
        ]
    ],
    'g',
    'h'
]

print(nested_list[2][2])        # ['ccc', 'ddd']
print(nested_list[2][2][0])     # eee

# SLICING A LIST
# A segment of a list is called a slice and you can extract one by using a
# slice operator. A slice of a list is also a list.

# The slice operator[n:m] returns the part of the list from the "n-th" item to
# the "m-th" item, including the first but excluding the last.

letters = ['a', 'b', 'c', 'd', 'e', 'f']

print(letters[2:5])     # ['c', 'd', 'e']
print(letters[0:2])     # ['a', 'b']
print(letters[3:-1])    # ['d', 'e']

# CHANGE ITEM VALUE
# You can replace an existing element with a new value by assigning the new
# value to the index.

ants = ['carpenter', 'fire', 'pharaoh']
ants[0] = 'tapinoma'
print(ants)             # ['tapinoma', 'fire', 'pharaoh']

ants[-1] = 'carpenter'
print(ants)             # ['tapinoma', 'fire', 'carpenter']


# ADD ITEMS TO A LIST
# To add new values to a list, use append() method. This method adds items only
# to the end of the list.
languages = ['Spanish', 'English', 'French']
print(languages)

languages.append('Chinese')
print(languages)

# If you want to insert an item at a specific position in a list, use insert()
# method. Note that all of the values in the list after the inserted value will
# be moved down one index.
languages = ['Spanish', 'English', 'French']
languages.insert(1, 'Chinese')
print(languages)

# COMBINE LISTS
# You can merge one list into another by using extend() method. It takes a list
# as an argument and appends all of the elements.
languages = ['Spanish', 'English']
print(languages)

languages.extend(['Chinese', 'French'])
print(languages)

# Alternatively, you can use the concatenation operator + or the augmented
# assignment operator +=

# Concatenation operator
languages = ['Spanish', 'English']
languages = languages + ['Chinese', 'French']
print(languages)

# Augmented assignment operator
languages = ['Spanish', 'English']
languages += ['Chinese', 'French']
print(languages)
