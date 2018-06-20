# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 20:00:19 2018

@author: Alicia
"""

a = "0.2"
b = "0.1"

print(float(a)+float(b))
print(repr(float(a)+float(b)))

print(a+b)

names=['zhang', 'liu', 'lin','xie']
print(names)

message = "my first friend is called: " + names[1].title() + "! I miss her."
print(message.title())

names[0] = 'Duan'
print(names)

second_friend = "my second friend is " + names.pop(0).title() + "!"
print(second_friend)

print(names)

#Removing an item by value
names.remove('liu')
print(names)

too_mean = 'xie'
names.remove(too_mean)
print(names)
print("\n\tThe one named " + too_mean.title() + " is too mean!")

#Sorting a list permanently with the sort() method
names=['zhang', 'liu', 'lin','xie']
names.sort()
print(names)

names.sort(reverse=True)
print(names)

#Sorting a list temporarily with a sorted function
names=['zhang', 'liu', 'lin','xie']
print("here is the original list: ")
print(names)

print("\nhere is the sorted list: ")
print(sorted(names))
print(sorted(names, reverse=True))

print("\nhere is the original list again: ")
print(names)

#printing a list in reverse order
names=['zhang', 'liu', 'lin','xie']
print(names)

names.reverse()
print(names)

#Finding the length of a list
names=['zhang', 'liu', 'lin','xie']
print(len(names))

#Avoiding index errors when working with lists
names=['zhang', 'liu', 'lin','xie']
print(names[-1])

#looping through an entire list
names=['zhang', 'liu', 'lin','xie']
for name in names:
    #without indented block, there will also be an error!
    print(name)
    print(name.title() + ", you're my friend!")
    print("I wish to see you again, " + name.title() + "!" )
 
#Good way to do a summary
print("\nThank you all for being my friends!")

#indenting unnessessarily
#message = ('\nhello world!')
#  print(message) An unexpected indent!

#making numerical lists
for value in range(1,5):
    print(value)
    
numbers=list(range(1,5))
print(numbers)

even_numbers=(range(2,11,2))
print(even_numbers)

_odd_numbers=(range(1,20,2))
print(_odd_numbers)

squares = []
for value in range(1,11):
    square = value**2
    print(square)
    squares.append(square)
print(squares)
#Page 63






    
    

