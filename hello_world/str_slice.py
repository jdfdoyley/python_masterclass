"""This file demonstrates how to use Python slice.
    """

#                1111111
#      01234567890123456
cat = "British Shorthair"

print(cat[0:7])     # British
print(cat[8:13])    # Short
print(cat[13:])     # hair
print(cat[:7])      # British
print(cat[8:])      # Shorthair
print(cat[:6] + cat[6:])    # British Shorthair
print(cat[:])       # British Shorthair
