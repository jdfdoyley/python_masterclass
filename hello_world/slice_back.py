"""This file demonstrates the slicing a string backwards"""

ALPHABETH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
backwards = ALPHABETH[25::-1]
print(backwards)

# Create a slice that produces the characters qpo.
print(ALPHABETH[16:13:-1])          # QPO

# Slice the string to produce edcba
print(ALPHABETH[4::-1])             # EDCBA

# Slice the string to produce the last 8 characters, in reverse order.
print(ALPHABETH[25:17:-1])          # ZYXWVUTS
print(ALPHABETH[:-9:-1])            # ZYXWVUTS

# Retrieve the last 4 characters in the string
print(ALPHABETH[-4:])               # WXYZ

# Retrieve the last character in the list
print(ALPHABETH[-1:])               # Z

# Retrieve the first character in the string
print(ALPHABETH[:1])                # A
