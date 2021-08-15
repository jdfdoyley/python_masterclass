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

# String Case Conversion
# Python provides five methods to perform case conversion on the target string
# viz lower(), upper(), capitalize(), swapcase(), and title().

string = "This is a String of Text."

# lower case
print(string.lower())

# UPPER CASE
print(string.upper())

# Capitalize case
print(string.capitalize())

# sWAP cASE
print(string.swapcase())

# Title Case
print(string.title())

# Check if Substring Contains in a String
# To check if a specific text is present in a string, use the in operator. The
# in is a boolean operator, which takes two strings and returns True if the
# first appears as a substring in the second

string = "The big red fox jumped over the lazy dog."
print("fox" in string)          # True
print("Dog" in string)          # False: case sensitive

# To search for a specific text within a string, use find() method. It returns
# the lowest index in the string where substring is found.
string = "Stay Hungry, Stay Foolish"
print(string.find("Foolish"))
print(string[string.find(("Foolish"))])
