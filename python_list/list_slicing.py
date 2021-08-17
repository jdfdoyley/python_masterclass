"""In this file I will demonstrate how Python list slicing works. """

# PYTHON LIST SLICING
# To access a range of items in a list, you need to slice a list. One way to do
# this is to use the simple slicing operator :

# With this operator you can specify where to start the slicing, where to end
# and specify the step.

# SLICING A LIST
# If list_var is a list, the expression list_var[start:stop:step] returns the
# portion of the list from index start to index stop, at a step size step.

# Basic Example
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[3:7])     # [3, 4, 5, 6]

print()

# SLICE WITH NEGATIVE INDICES
# You can also specify negative indices while slicing a list.
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[-7:-3])   # [3, 4, 5, 6]

print()

# SLICE WITH POSITIVE & NEGATIVE INDICES
# You can specify both positive and negative indices at the same time.
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[-7:7])    # [3, 4, 5, 6]

print()

# SPECIFY STEP OF THE SLICING
# You can specify the step of the slicing using step parameter. The step
# parameter is optional and by default 1.
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[0::1])
print(numbers[::2])     # [0, 2, 4, 6, 8]
print(numbers[::3])     # [0, 3, 6, 9]

print()

# Negative Step Size
# You can also specify a negative step size.
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[::-2])    # [9, 7, 5, 3, 1]
print(numbers[-2::-2])  # [8, 6, 4, 2, 0]
print(numbers[7:2:-1])  # [7, 6, 5, 4, 3]
print(numbers[3:8:-1])  # []

print()

# SLICE AT BEGINNING & END
# Omitting the start index starts the slice from the index 0. Meaning, L[:stop]
# is equivalent to L[0:stop]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[:5])      # [0, 1, 2, 3, 4]

# Whereas, omitting the stop index extends the slice to the end of the list.
# Meaning, L[start:] is equivalent to L[start:len(L)]

# Print the last 5 elements of the list
print(numbers[5:])      # [5, 6, 7, 8, 9]

index = round(len(numbers) / 2)
print(numbers[index:])      # [5, 6, 7, 8, 9]

print()

# REVERSE A LIST
# You can reverse a list by omitting both start and stop indices and specifying
# a step as -1.
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[::-1])        # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print()

# MODIFY MULTIPLE LIST VALUES
# You can modify multiple list items at once with slice assignment. This
# assignment replaces the specified slice of a list with the items of assigned
# iterable.

# Modify multiple list items
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)

numbers[:3] = [9, 8, 7]
print(numbers)

numbers[7:] = [0, 1, 2]
print(numbers)          # [9, 8, 7, 3, 4, 5, 6, 0, 1, 2]

numbers[3:4] = [0, -1, -2, -3]
print(numbers)          # [9, 8, 7, 0, -1, -2, -3, 4, 5, 6, 0, 1, 2]

middle = round(len(numbers) / 2)
numbers[middle:middle] = [2, 4, 6]
print(numbers)
