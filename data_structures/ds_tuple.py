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
