# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 20:28:49 2018

@author: Alicia
"""

bicycles = ['trek', 'red line', 'specialized']
print(bicycles)

#Accessing elements in a list, Index Positions Start at 0, Not 1
print(bicycles[0])
print(bicycles[-1].title())

message = "my bicycle was a " + bicycles[-1].title() + "."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#Adding elements to a list
motorcycles.append('sdf')
print(motorcycles)

motorcycles = []
motorcycles.append('sdf')
motorcycles.append('gdgfdg')
print(motorcycles)

#inserting elements into a list
motorcycles.insert(0, 'dgfd')
motorcycles.insert(3, 'qwe')
print(motorcycles)

#Removing elements from a list
del motorcycles[1]
print(motorcycles)

#Removing an Item Using the pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle) #This is to show that we still have access to the value that we popped.



