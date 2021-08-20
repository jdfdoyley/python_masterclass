# pylint: disable=C0103
"""In this file I demonstrate Python Dictionary."""

# CREATE A DICTIONARY
# You can create a dictionary by placing a comma-separated list of key:value
# pairs in curly braces {}. Each key is separated from its associated value by
# a colon :

# Create a dictionary to store employee records
emp = {
    'name': 'jason',
    'age': 31,
    'job': 'front office manager',
    'city': 'norfolk',
    'email': 'jason@email.com'
}

print(emp)

print()

# THE dict() CONSTRUCTOR
# You can convert two-value sequences into a dictionary with Python's dict()
# constructor. The first item in each sequence is used as the key and the
# second as the value.

# Create a dictionary with a lit of two-item tuples
list_tuple = [
    ('name', 'jason'),
    ('age', 31),
    ('job', 'software engineer')
]

emp = dict(list_tuple)
print(emp)
print()

# Create a dictionary with a tuple of two-item lists
tuple_list = (
    ['name', 'jason'],
    ['age', 31],
    ['job', 'software engineer']
)

emp = dict(tuple_list)
print(emp)
print()

# When the keys are simple strings, it is sometimes easier to specify key:value
# pairs using keyword arguments.
emp = dict(
    name='jason',
    age=25,
    job='Dev'
)

print(emp)
print()

# OTHER WAYS TO CREATE DICTIONARIES
# There are lots of other ways to create a dictionary.

# You can use dict() function along with the zip() function, to combine
# separate list of keys and values obtained dynamically at runtime.

# Create a dictionary with list of zipped keys/values
keys = ['first', 'last', 'age', 'position']
values = ['jason', 'doyley', 31, 'frontend dev']

emp = dict(zip(keys, values))
print(emp)
print()

# You'll often want to create a dictionary with default values for each key.
# The fromkeys() method offers a way to do this.

# Initialize dictionary with default value '0' for each key
keys = ['first', 'last', 'age', 'position']
defaultValue = 0

emp = dict.fromkeys(keys, defaultValue)
print(emp)
print()
