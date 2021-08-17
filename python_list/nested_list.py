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

print()

# CHANGE NESTED LIST ITEM VALUE
# You can change the value of a specific item in a nested list by referring to
# its index number.
author = ['Lee', 'Child', ['Killing Floor', 'No Middle Name', 'Die Trying']]
print(f'Original list: {author}')

author[2][1] = 'Tripwire'
print(f'New list: {author}')

print()

# ADD ITEMS TO A NESTED LIST
# To add new values to the end of the nested list, use append() method.
author = ['Lee', 'Child', ['Killing Floor', 'Die Trying']]
print(f'Original list: {author}')

author[2].append('Tripwire')
print(f'New list: {author}')

print()

# When you want to insert an item at a specific position in a nested list, use
# insert() method.
author = ['Lee', 'Child', ['Killing Floor', 'Tripwire']]
print(f'Original list: {author}')

author[2].insert(1, 'Die Trying')
print(f'New list: {author}')

print()

# You can merge one list into another by using extend() method.
author = ['Lee', 'Child', ['Killing Floor', 'Tripwire'], 66]
genres = ['Crime fiction', 'mystery', 'thriller']
others = ['The Snake Eater by the Numbers', 'Ten Keys',
          'The Greatest Trick of All', 'Safe Enough', 'The .50 Solution']

print(f'Original list: {author}')

# Insert genres after the age object in the list
author.append(genres)
print(f'New list: {author}')

# Extend the list to add some other books by Lee Child
author[2].extend(others)
print(f'Newer list: {author}')

print()

# REMOVE ITEMS FROM A NESTED LIST
# If you know the index of the item you want, you can use pop() method. It
# modifies the list and returns the removed item.
author = ['Lee', 'Child', ['Killing Floor', 'No Middle Name', 'Die Trying']]
print(f'Original list: {author}')

deleted_item = author[2].pop(1)
print(f'New list: {author}')
print(f'Deleted Item: {deleted_item}')
print()

# If you don’t need the removed value, use the del statement.
author = ['Lee', 'Child', ['Killing Floor', 'No Middle Name', 'Die Trying']]
print(f'Original list: {author}')

del author[2][1]
print(f'New list: {author}')
print()

# If you’re not sure where the item is in the list, use remove() method to
# delete it by value.
author = ['Lee', 'Child', ['Killing Floor', 'No Middle Name', 'Die Trying']]
print(f'Original list: {author}')

author[2].remove('No Middle Name')
print(f'New list: {author}')

print()

# FIND THE NESTED LIST LENGTH
# You can use the built-in len() function to find how many items a nested
# sublist has.
author = ['Lee', 'Child', ['Killing Floor', 'Tripwire'], 66]
others = ['The Snake Eater by the Numbers', 'Ten Keys',
          'The Greatest Trick of All', 'Safe Enough', 'The .50 Solution']

# Find the lenth of the original nested list
print(f'Original list: {author}')
print(f"Length of Original Nested List: {len(author[2])}")

print()

author[2].extend(others)
print(f'New list: {author}')
print(f"Length of New Nested List: {len(author[2])}")
