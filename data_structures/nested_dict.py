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
employees1 = {
    'emp1': {'name': 'Bob', 'job': 'Mgr'},
    'emp2': {'name': 'Kim', 'job': 'Dev'},
    'emp3': {'name': 'Sam', 'job': 'Dev'}
}

# THE dict() CONSTRUCTOR
# There are several ways to create a nested dictionary using a type constructor
# called dict().

# To create a nested dictionary, simply pass dictionary key:value pair as
# keyword arguments to dict() Constructor.
employees2 = dict(
    emp1={'name': 'Bob', 'job': 'Mgr'},
    emp2={'name': 'Kim', 'job': 'Dev'},
    emp3={'name': 'Sam', 'job': 'Dev'}
)
print(employees2)
print()

# You can use dict() function along with the zip() function, to combine
# separate lists of keys and values obtained dynamically at runtime.
ids = ['emp1', 'emp2', 'emp3']
emp_info = [
    {'name': 'Bob', 'job': 'Mgr'},
    {'name': 'Kim', 'job': 'Dev'},
    {'name': 'Sam', 'job': 'Dev'},
]

employees3 = dict(zip(ids, emp_info))
print(employees3)
print()

# You’ll often want to create a dictionary with default values for each key.
# The fromkeys() method offers a way to do this.
ids = ['emp1', 'emp2', 'emp3']
default_values = {'name': '', 'job': ''}

employees4 = dict.fromkeys(ids, default_values)
print(employees4)
print()
