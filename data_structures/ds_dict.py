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

# IMPORTANT PROPERTIES OF A DICTIONARY

# Keys must be unique:
# A key can appear in a dictionary only once.

# Even if you specify a key more than once during the creation of a dictionary,
# the last value for that key becomes the associated value.
# emp = {
#     'name': 'Jason',
#     'age': 31,
#     'name': 'Bob'
# }
# print(emp)      # {'name': 'Bob', 'age': 31}
# print()

# Key must be immutable type:
# You can use any object of immutable type as dictionary keys - such as
# numbers, strings, booleans or tuples.
ds_dict = {(2, 2): 25,
           True: 'a',
           'name': 'Bob'}

print(ds_dict)
print()

# An exception is raised when mutable object is used as a key
# ds_dict = {[2, 2]: 25,
#            'name': 'Bob'}

# print(ds_dict)  # TypeError: unhashable type: 'list'
# print()

# Value can be of any type
# There are no restrictions on dictionary values. A dictionary value can be any
# type of object and can appear in a dictionary multiple times.

# values of different datatypes
ds_dict1 = {'a': [1, 2, 3],
            'b': [1, 2, 3]}
print(ds_dict1)
print()

ds_dict2 = {'a': [1, 2],
            'b': [1, 2],
            'c': [1, 2]}
print(ds_dict2)
print()

# ACCESS DICTIONARY ITEMS
# The order of key:value pairs is not always the same. In fact, if you write
# the same example on another PC, you may get a different result. In general,
# the order of items in a dictionary is unpredictable.

# But this is not a problem because the items of a dictionary are not indexed
# with integer indices. Instead, you use the keys to access the corresponding
# values.

# You can fetch a value from a dictionary by referring to its key in square
# brackets [].
emp = {
    'name': 'jason',
    'age': 31,
    'job': 'front office manager',
    'city': 'norfolk',
    'email': 'jason@email.com'
}

print(emp['name'].title())
print(emp['job'].title())
print()

# If refer to a key that is not in the dictionary, you'll get an exception
# print(emp['salary'])        # KeyError: 'salary'

# To avoid such exception, you can use the special dictionary get() method.
# This method returns the value for key if key is in the dictionary, else None,
# so that this method never raises a KeyError

# When the key is present
print(emp.get('name').title())

# When the key is absent
print(emp.get('salary'))
print()

# ADD OR UPDATE DICTIONARY ITEMS
# Adding or updating dictionary items is easy. Just refer to the item by its
# key and assign a value. If the key is already present in the dictionary, its
# value is replaced by the new one.
emp = {
    'name': 'jason',
    'age': 31,
    'job': 'front office manager',
    'email': 'jason@email.com'
}
emp['age'] = 28
print(emp)

# If the key is new, it is added to the dictionary with its value
emp['city'] = 'new york'
print(emp)
