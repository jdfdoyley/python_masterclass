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

# ACCESS NESTED DICTIONARY ITEMS
# You can access individual items in a nested dictionary by specifying key in
# multiple square brackets.
employees5 = {
    'emp1': {'name': 'Bob', 'job': 'Mgr'},
    'emp2': {'name': 'Kim', 'job': 'Dev'},
    'emp3': {'name': 'Sam', 'job': 'Dev'}
}

# Get the name of the first employee
print(employees5['emp1']['name'])           # Bob

# Get the job of the third employee
print(employees5['emp3']['job'])            # Dev
print()

# If you refer to a key that is not in the nested dictionary, an exception is
# raised.
# print(employees5['emp1']['salary'])       # KeyError: 'salary'

# To avoid such exception, you can use the special dictionary get() method.
# This method returns the value for key if key is in the dictionary, else None,
# so that this method never raises a KeyError.

# key present
print(employees5['emp1'].get('name'))           # Bob

# key absent
print(employees5['emp2'].get('salary'))         # None
print()

# CHANGE NESTED DICTIONARY ITEMS
# To change the value of a specific item in a nested dictionary, refer to its
# key.
employees6 = {
    'emp1': {'name': 'Bob', 'job': 'Mgr'},
    'emp2': {'name': 'Kim', 'job': 'Dev'},
    'emp3': {'name': 'Sam', 'job': 'Dev'}
}
employees6['emp1']['name'] = 'Pam'
employees6['emp1']['job'] = 'Eng'

print(employees6['emp1'])
print()

# ADD OR UPDATE NESTED DICTIONARY ITEMS
# Adding or updating nested dictionary items is easy. Just refer to the item by
# its key and assign a value. If the key is already present in the dictionary,
# its value is replaced by the new one.
employees7 = {
    'emp1': {'name': 'Bob', 'job': 'Mgr'},
    'emp2': {'name': 'Kim', 'job': 'Dev'},
    'emp3': {'name': 'Sam', 'job': 'Dev'}
}

employees7['emp2'] = {'name': 'Ari', 'job': 'Designer'}

print(employees7)
print()

# If the key is new, it is added to the dictionary with its value.
employees7['emp2'] = {'name': 'Ari', 'job': 'Designer', 'salary': 104000.0}
print(employees7)
print()

# MERGE TWO NESTED DICTIONARIES
# Use the built-in update() method to merge the keys and values of one nested
# dictionary into another. Note that this method blindly overwrites values of
# the same key if there’s a clash.
employees8 = {
    'emp1': {'name': 'Bob', 'job': 'Mgr'},
    'emp2': {'name': 'Kim', 'job': 'Dev'},
}

employees9 = {
    'emp2': {'name': 'Sam', 'job': 'Dev'},
    'emp3': {'name': 'Ari', 'job': 'Designer'}
}

print("List 1:", employees8)
print("List 2:", employees9)
print()

# Here the ’emp2′ record is updated while ’emp3′ is added to the dictionary.
employees8.update(employees9)
print("Merge List:", employees8)
print("Number of Items:", len(employees8))
print()

# REMOVE NESTED DICTIONARY ITEMS
# There are several ways to remove items from a nested dictionary.

# Remove an Item by Key
# If you know the key of the item you want, you can use pop() method. It
# removes the key and returns its value.
employees10 = {
    'emp1': {'name': 'Bob', 'job': 'Mgr'},
    'emp2': {'name': 'Kim', 'job': 'Dev'},
    'emp3': {'name': 'Sam', 'job': 'Dev'}
}

# Remove emp2 from the list
removed_item = employees10.pop('emp2')

print("Updated List:", employees10)
print("Removed Item:", removed_item)
print()
