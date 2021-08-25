"""This file demonstrate the use of Python Set."""

# PYTHON SET
# Python set is an unordered collection of unique items. They are commonly used
# for computing mathematical operations such as union, intersection,
# difference, and symmetric difference.

# The important properties of Python sets are as follows:

# Sets are unordered – Items stored in a set aren’t kept in any particular
# order.
# Set items are unique – Duplicate items are not allowed.
# Sets are unindexed – You cannot access set items by referring to an index.
# Sets are changeable (mutable) – They can be changed in place, can grow and
# shrink on demand.

# CREATE A SET
# ------------
# You can create a set by placing a comma-separated sequence of items in curly
# braces {}

# A set of strings
colors = {'red', 'green', 'blue'}

# A set of missed datatypes
employee_info = {12345, "James Brown", 405445.32, True}

# Sets don't allow duplicates. They are automatically removed during creation
# of a set.
colors = {'red', 'blue', 'green', 'red'}
print(colors)               # {'blue', 'red', 'green'}

# A set itself is mutable (changeable), but it cannot contain mutable objects.
# Therefore, immutable objects like numbers, strings, tuples can be a set item,
# but lists and dictionaries are mutable, so they cannot be.

# Valid set items
S = {1, 'abc', ('a', 'b'), True}

# Invalid set items
# S = {[1, 2], {'a': 1, 'b': 2}}  # TypeError: unhashable type: 'list'
