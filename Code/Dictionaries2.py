# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 15:01:28 2018

@author: p511ybu
"""

#page 93 TRY IT YOURSELF
usernames = ['Lars', 'Anton', 'May', 'Anna', 'Tara', 'admin']
for username in usernames:
    if username == 'admin':
      print("Welcome! admin! Have a nice day at work!")
    else:
      print("Welcome, " + username + " !")
          
usernames = []
if usernames:
    for username in usernames:
        print("Welcome to work! Pigg och glad!")
    print("\nConfiguration completed!")
else:
    print("\nWe need to find some users!")
    
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print("Original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
    
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position: " + str(alien_0['x_position']))

#Removing key-value Pairs
del alien_0['y_position'] #This value is removed permanently.
print(alien_0)

#A dictionary of similar objects
favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }
print("jen's favorite language is " + favorite_languages['jen'].title() + ".")

#Looping through a dictionary
#Looping through all key-value pairs
for key, value in favorite_languages.items():
    print(key)
    print(value)
    
#Looping through all the keys in a dictionary
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        print("Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!" )
    