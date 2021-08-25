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

# SET CONSTRUCTOR
# You can also create a set using a type constructor called set()

# Set of items in a iterable
strings = set('abc')
print(strings)

# Set of successive integers
integers = set(range(0, 4))
print(integers)

# Convert a list into a set
lists = set([1, 3, 5, 7, 9])
print(lists)

# ADD ITEMS TO A SET
# You can add a single item to a set using the add() method.
orchids = {'moth', 'boat', 'vanda', 'cattleya', 'slipper'}

# Add a sixth orchid to the set
orchids.add('venus')
print(orchids)

# You can add multiple items to a set using the update() method.
# Add three more types of orchid to the set
orchids.update(['dancing-lady', 'flat-leaved', "nun's hood"])
print(orchids)

# REMOVE ITEMS FROM A SET
# To remove a single item from a set, use the remove() or discard() method.

# using the remove() method, remove the vanda orchid from the set
orchids = {'moth', 'boat', 'vanda', 'cattleya', 'slipper',
           'dancing-lady', 'flat-leaved', "nun's hood", 'venus'}
orchids.remove('vanda')
print(orchids)

# using the discard method, remove the flat-leaved orchid from the set
orchids.discard('flat-leaved')
print(orchids)

# Note: remove() vs discard()
# Both methods work exactly the same. The only difference is that If specified
# item is not present in a set:
#       remove() method raises KeyError
#       discard() method does nothing

# The pop() method removes random item from a set and returns it

# Randomly remove an item from the set and then return it to the user
popped_item = orchids.pop()
print(orchids)
print(f"Popped Item: {popped_item}")

# To remove all the items from a set, the clear() method is recommened

# Remove all the items from the orchid set
orchids.clear()
print(orchids)
