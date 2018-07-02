# -*- coding: utf-8 -*-
"""
Created on Mon Jul 02 14:14:54 2018

@author: Alicia
"""

#Review distionary

favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
   }
   
print("The following labguages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())
    
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
#Use set() to pull out the unique languages in favorite_languages.values().
#User input: how to accept user input so your program can then work with it.
#In CMD-python

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
     continue
    print("\t" + str(current_number))

x = 1
while x <= 5:
  print(x)
  x += 1
# This loop runs forever!
x = 1
while x <= 5:
   print(x)
   break





