# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 13:17:03 2018

@author: p511ybu
"""

# The Python Standard Library
from collections import OrderedDict
# module: collections
# class OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
   print(name.title() + "'s favorite language is " +
      language.title() + ".")

# Reading an Entire File 
with open('pi_digits.txt') as file_object:
   contents = file_object.read()
   print(contents)
   
with open('pi_digits.txt') as file_object:
   contents = file_object.read()
   print(contents.rstrip())
# Using absolute paths, you can read files from any location on your system.
   
# Reading Line by Line
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
      print(line) 
      
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
      print(line.rstrip())
      
# Making a List of Lines from a File
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines() #the readlines() method takes each line from the file and 
# stores it in a list. This list is then stored in lines, which we can continue to work with
# after the with block ends.
    
for line in lines:
   print(line.rstrip())
   
# Working with a File’s Contents
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
    # We then create a loop that adds each line of digits to
    # pi_string and removes the newline character from each line.
    
print(pi_string)
print(len(pi_string))

# get rid of that by using strip() instead of rstrip()
filename = 'pi_digits.txt'
with open(filename) as file_object:
   lines = file_object.readlines()

pi_string = []
for line in lines:
  pi_string += line.strip()
   
print(pi_string)
print(len(pi_string))

#Page 195