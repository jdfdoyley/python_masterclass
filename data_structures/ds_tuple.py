"""This is about Python Tuple"""

# CREATE A TUPLE
# You can create a tuple by placing a comma-separated sequence of items in
# parentheses ().

# A Tuple of integers
integers = (1, 2, 3, 4, 5, 6)

# A tuple of strings
sharks = ("Hammerhead", "Sand", "Sawshark", "Ccatshark", "Cow")

# The items of a tuple don’t have to be the same type.
mixed = (1, 3.14, True, "Harry")

# A tuple containing zero items is called an empty tuple and you can create one
# with empty brackets ()
empty = ()

# SINGLETON TUPLE
# If you have only one value in a tuple, you can indicate this by including a
# trailing comma , just before the closing parentheses.
singleton_tuple = ('Hammerhead',)
print(type(singleton_tuple))

# THE tuple() CONSTRUCTOR
# You can convert other data types to tuple using Python’s tuple() constructor.

# Convert a string to a tuple
int_tuple = tuple([1, 2, 3, 4, 5, 6])
print(int_tuple)

# Convert a string to a tuple
shark = tuple('Sawshark')
print(shark)

# NESTED TUPLES
# A tuple can contain sub-tuple, which in turn can contain sub-tuples
# themselves, and so on. This is known as nested tuple. You can use them to
# arrange data into hierarchical structures.
nested_tuple = ('red', ('green', 'blue'), 'yellow')

# TUPLE PACKING
# When a tuple is created, the items in the tuple are packed together into the
# object.
sharks = ("Hammerhead", "Sand", "Sawshark", "Ccatshark", "Cow")
print(sharks)

# TUPLE UNPACKING
# When a packed tuple is assigned to a new tuple, the individual items are
# unpacked (assigned to the items of a new tuple).
sharks = ("Hammerhead", "Sand", "Sawshark", "Catshark", "Cow")
(a, b, c, d, e) = sharks

print(a)
print(b)
print(c)
print(d)
print(e)
