# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 19:07:46 2018

@author: Alicia
"""

digits=list(range(0,10))
print(digits)

print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in list(range(1,11))]
print(squares)

print("The following is reversed version: ")
squares.sort(reverse=True)
print(squares)

print(sorted(squares, reverse=True))

squares.reverse()
print(squares)

#Working with Part of a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[2:3])

print("\nHere are the first three players on my team:")
print(players[:3])
print(players[2:])
print("\nThe last 3 players in the list: ")
print(players[-3:])

#Looping Through a Slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
 print(player.title())
 
#Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods == friend_foods)

#To prove that we actually have two separate lists
my_foods = ['pizza', 'falafel', 'cake']
friend_foods = my_foods[-2:]
my_foods.append('ice cream')
print(my_foods)
print(friend_foods)

#Tuples
#Define a tuple
dimensions = (200,50)
print(dimensions[0])
print(dimensions[-2])

#dimensions[0]=250
#This throws an error. Basically, because we’re trying to alter a tuple, which can’t be done to that type of object, Python tells us we can’t assign a new value to an item in a tuple
#Page 70