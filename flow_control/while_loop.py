"""In this file, I will demonstrate the use of Python while Loops."""
# pylint: disable=C0103

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

print()

# BREAK IN WHILE LOOP
# Python break statement is used to exit the loop immediately. It simply jumps
# out of the loop altogether, and the program continues after the loop.

# Exit when x becomes 3
x = 6
while x:
    print(x)
    x -= 1
    if x == 3:
        break

print()

# CONTINUE IN WHILE LOOP
# The continue statement skips the current iteration of a loop and continues
# with the next iteration.

# Skip odd numbers
x = 6
while x:
    x -= 1
    if x % 2 != 0:
        continue
    print(x)

print()

# ELSE IN WHILE LOOP
# Python allows an optional else clause at the end of a loop. The else clause
# will be executed when the loop terminates normally (the condition becomes
# false).

# pylint: disable=W0120
x = 6
while x:
    print(x)
    x -= 1
else:
    print("Done!")

print("After the else block")
print()

# The else clause will still be executed if the condition is false at the start.
x = 0
while x:
    print(x)
    x -= 1
else:
    print('Done!')

print("After the else block")
print()

# If the loop terminates prematurely with break, the else clause won’t be
# executed.
x = 6
while x:
    print(x)
    x -= 1
    if x == 3:
        break
else:
    print('Done!')

print("After the else block")
