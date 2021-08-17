"""In this file I will demonstrate Nested List in Python."""

# A nexted list is when one list contains a sublist which can also contains
# another sublist.

# You can use them to arrange data in a hirarchical structure.

# CREATE A NESTED LIST
# A nexted list is created by placing a comma-separated sequence of sublists.
nested_list = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', 'h']
print(nested_list)

print()

# ACCESS NESTED LIST ITEMS BY INDEX
# You can access individual items in a nested list using multiple indexes.
nested_list = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
print(nested_list[2])
print(nested_list[2][2])
print(nested_list[2][2][0])

print()

# NEGATIVE LIST INDEXING IN A NESTED LIST
# You can access a nested list by negative indexing as well.
# Negative indexes count backward from the end of the list. So, L[-1] refers to
# the last item, L[-2] is the second-last, and so on.
nested_list = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']

print(nested_list[-3])
print(nested_list[-3][-1])
print(nested_list[-3][-1][-2])
