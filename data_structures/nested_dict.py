"""This file is used to demonstrate Python Nested Dictionary."""

# PYTHON NESTED DICTIONARY
# A dictionary can contain another dictionary, which in turn can contain
# dictionaries themselves, and so on to arbitrary depth. This is known as
# nested dictionary.

# Nested dictionaries are one of many ways to represent structured information
# (similar to ‘records’ or ‘structs’ in other languages).

# CREATE A NESTED DICTIONARY
# A nested dictionary is created the same way a normal dictionary is created.
# The only difference is that each value is another dictionary.

# Let’s build a dictionary that stores employee record.
employee = {
    'emp1': {'name': 'Bob', 'job': 'Mgr'},
    'emp2': {'name': 'Kim', 'job': 'Dev'},
    'emp3': {'name': 'Sam', 'job': 'Dev'}
}
