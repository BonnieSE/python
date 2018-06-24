# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 09:16:36 2018

@author: Alicia
"""

dimensions = (200,50,70,12,0)
print(dimensions[-5])
print(dimensions[-1])

#writing over a tuple
print("Original dimensions: ")
for value in dimensions:
    print(value)
    
dimensions = (400,100) #We store a new tuple in the variable dimensions
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)
#When compared with lists, tuples are simple data structures. Use them
#when you want to store a set of values that should not be changed throughout
#the life of a program.

#Styling you code: Python Enhancement Proposal (PEP).
#1. PEP 8 recommends that you use four spaces per indentation level
#2. Many Python programmers recommend that each line should be less than 80 characters.
#3. To group parts of your program visually, use blank lines.

#if statements
cars = ['audi', 'volvo', 'toyota']
for car in cars:
    if car=='audi':
        print(car.upper())
    else:
        print(car.title())
        
#Conditional tests
car='bmw'
print(car=='bmw')

#Ignoring Case When Checking for Equality
car='AUDI'
print(car=='audi')
print(car.lower()=='audi')
print(car)

#Checking for Inequality
car='audi'
if car != 'Audi':
    print("Does not match!")
else:
    print("match!")
    
#Numerical Comparisons
age=18
print(age==18)

age=17
if age!=18:
    print("The age is wrong!")
    
age=19
print(age<21)
print(age>21)
print(age>=19)
