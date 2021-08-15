"""This file demonstrate how to use strings in Python"""

print("Today is a good day to learn Python")
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')
print("Hello" + " Jason!")

greeting = "Hello"
name = "Dave"
# name = input("Please enter your name: ")
print(greeting + " " + name)

age = 24
print(age)

print(type(greeting))
print(type(age))

age_in_words = "2 years"
# TypeError: can only concatenate str (not "int") to str
# print(name + " is " + age + " years old.")
print(name + " is " + age_in_words + " years old.")
print(type(age))

# Find String Length
# To find the number of characters in a string, use len() built-in function

string = "Supercalifragilisticexpialidocious"
print(len(string))

# Replace Text Within a String
# Sometimes you want to replace a text inside a string, then you can use the
# replace() method

string = "Hello, World!"
str_replace = string.replace('World', 'Universe')

print(str_replace)

# Split and Join a String
# Use split() method to chop up a string into a list of substrings, around a
# specified delimiter.

# Split the string on comma
string = "red,green,blue,yellow"
str_split = string.split(',')
print(str_split)

# Use join() method to join the list back into a string, with a specified
# delimiter in between.

#  Join the list of substrings
str_list = ["red", "green", "blue", "yellow"]
string = ",".join(str_list)
print(string)
