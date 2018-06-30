# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 22:05:03 2018

@author: Alicia
"""

#Looping through a dictionary's key's in order
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'}

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
    
#Looping through all values in a dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'}

print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())  #P 107 ???
    
print("\n\tThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
    
#Nesting: a list of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
    


    
    