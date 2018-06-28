# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 19:48:25 2018

@author: Alicia
"""

#Dictionaries
alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0['color'])
print(alien_0['points'])

#dictionary: a collection of key-value pairs
#Accessing values in a dictionary
alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0['color'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

#Adding new Key value pairs
alien_0['x'] = 0
alien_0['y'] = 23
print(alien_0['x'])
print(alien_0['y'])
print(alien_0)

#starting with an empty dictionary
alien_0 = {}
alien_0['sd'] = 23
alien_0['credits'] = 'good'
print(alien_0)

#Modifying values in a dictionary
alien_0 = {'color' : 'green'}
alien_0 = {'color' : 'red'}


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
  x_increment = 1
elif alien_0['speed'] == 'medium':
  x_increment = 2
else:
# This must be a fast alien.
  x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

#page 99