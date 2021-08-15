"""This file demonstrate how to use different operators with string."""

str_1 = "he's "
str_2 = "probably "
str_3 = "pining "
str_4 = "for the "
str_5 = "fjords."

print(str_1 + str_2 + str_3 + str_4 + str_5)
print("he's " "probably " "pining " "for the " "fjords.")

print("Hello " * 5)
# TypeError: can only concatenate str (not "int") to str
# print("Hello " * 5 + 4)
print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

today = "Friday"
print("day" in today)           # True
print("Fri" in today)           # True
print("fri" in today)           # False: case-sensitive
print("thur" in today)          # False
print("fish" in "cat")          # False
