# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 14:47:23 2018

@author: p511ybu
"""

# Writing to a File
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")   
# Writing Multiple Lines
    file_object.write("\nI love creating new games.")
    
    
    filename = 'programming.txt'
# Appending to a File
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets. \n")
    file_object.write("I love creating apps that can run in browser. \n")
    
# Exceptions: manage errors. Handled with try-except blocks.
# Handling the ZeroDivisionError Exception
try:
   print(5/0)
except ZeroDivisionError:
   print("You can't divide by zero!")

# Using Exceptions to Prevent Crashes
print("Give me 2 numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number =='q':
        break
    
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    
    answer = int(first_number) / int(second_number)
    print(answer)
    
# The else Block
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number =='q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
