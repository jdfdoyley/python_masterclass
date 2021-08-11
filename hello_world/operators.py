"""This file demonstrate the use of valid Python operators and expressions."""

num_1 = 12
num_2 = 3

# Operator Demo
print(num_1 + num_2)    # 15
print(num_1 - num_2)    # 9
print(num_1 * num_2)    # 36
print(num_1 / num_2)    # 4.0
print(num_1 // num_2)   # 4 => integer division: round to minu infinity
print(num_1 % num_2)    # 0 => modulo: returns the remainder from a division

print()

for i in range(1, 4):
    print(i)

for i in range(1, num_1 // num_2):
    print(i)

print(num_1 + num_2 / 3 - 4 * 12)       # 35.0
print(num_1 + (num_2 / 3) - (4 * 12))   # 35.0
print((((num_1 + num_2) / 3) - 4) * 12)  # 12.0
