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

print()

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

print()

# SIGNIFICANCE OF INDENTATION
# Indentation has a special significance in Python. It is used to define a
# block of code (often referred to as, a suite). Contiguous statements that are
# indented to the same level are considered as part of the same block.

# if statement without indentation raises syntax error.

# NESTED IF STATEMENT
# You can nest statements within a code block to begin a new code block, as
# long as they follow their respective indentations.
x, y, z = 7, 4, 2
if x > y:
    print('x is greater than y')
    if x > z:
        print('x is greater than y and z.')

print()

# THE ELSE STATEMENT
# Use else statement to execute a block of Python code, if the condition is
# false.
x, y = 7, 5
if x < y:
    print('y is greater')
else:
    print('x is greater')

print()

# THE ELIF(ELSE IF) STATEMENT
# Use elif statement to specify a new condition to test, if the first condition
# is false.
x, y = 5, 5
if x > y:
    print('x is greater')
elif x < y:
    print('y is greater')
else:
    print('x and y are equal')

print()

# SUBSTITUTE FOR SWITCH CASE
# Unlike other programming languages, Python does not have a ‘switch‘
# statement. You can use if…elif…elif sequence as a substitute.
choice = 0

if choice == 1:
    print('case 1')
elif choice == 2:
    print('case 2')
elif choice == 3:
    print('choice 3')
elif choice == 4:
    print('choice 4')
else:
    print('default case')
