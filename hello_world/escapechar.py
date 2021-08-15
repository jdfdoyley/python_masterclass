"""This file demonstrates how to use the different escape characters."""

split_string = "This string has been\nsplit over\nseveral\nlines"
print(split_string)

tabbed_string = "1\t2\t3\t4\t5"
print(tabbed_string)

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")
print("""The pet shop owner said "No, no, \
'e's uh,...he's resting".""")

another_split_string = """This string has been
split over
several
lines"""
print(another_split_string)

another_split_string_2 = """This string has been \
split over \
several \
lines"""
print(another_split_string_2)

print("C:\\Users\\tommy\\notes.txt")
print(r"C:\Users\tommy\notes.txt")
