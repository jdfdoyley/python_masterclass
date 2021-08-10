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
