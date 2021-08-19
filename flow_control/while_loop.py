"""In this file, I will demonstrate the use of Python while Loops."""

# PYTHON WHILE LOOP
# A while loop is used when you want to perform a task indefinitely, until a
# particular condition is met. It’s a condition-controlled loop.

# SYNTAX

# while condition:
#     statement
#     statement
#     ...
# else:
#     statement
#     statement
#     ...

# BASIC EXAMPLES
# Any non-zero value or nonempty container is considered TRUE; whereas Zero,
# None, and empty container is considered FALSE.

# Iterate until x becomes 0
x = 6
while x:
    print(x)
    x -= 1

print()

# Iterate until list is empty
sharks = ["hammerhead", "sand", "sawshark", "catshark", "cow"]
while sharks:
    print(sharks.pop())

print()

# Iterate until string is empty
shark = "hammerhead"
while shark:
    print(shark)
    shark = shark[1:]

print()

# If the condition is false at the start, the while loop will never be executed
# at all.

# Exit condition is false at the start
x = 0
while x:
    print(x)
    x -= 1
