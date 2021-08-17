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
