"""In this file I will demonstrate the use of Python's if, elif and else statements."""

# PYTHON IF ELSE ELIF STATEMENT
# You can use following conditional statements in your code to do this.

# * if Statement: use it to execute a block of code, if a specified condition is
#  true

# * else Statement: use it to execute a block of code, if the same condition is
# false

# * elif (else if) Statement: use it to specify a new condition to test, if the
# first condition is false

# THE IF STATEMENT
# Use if statement to execute a block of code, if the condition is true.
x = 7
y = 5
if x > y:
    print('x is greater')

# In Python, any non-zero value or nonempty container is considered TRUE,
# whereas Zero, None, and empty container is considered FALSE. That’s why all
# the below if statements are valid.

# any non-zero value
if -3:
    print(True)

# mathematical expression
x, y = 7, 5
if x + y:
    print(True)

# nonempty container
my_list = [1, 2, 3, 4, 5]
if my_list:
    print(True)
