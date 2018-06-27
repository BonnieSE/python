# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 20:26:45 2018

@author: Alicia
"""

#Checking that a list is not empty
requested_students=[]
if requested_students:
    for requested_student in requested_students:
        print("Invite " + requested_student + " to the exam.")
else:
    print("Are you sure you don't invite any candidate?")
        
#Using multiple lists
available_toppings = ['mushrooms', 'olivers', 'green peppers', 'pepperoni']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']    
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + " on the pizza.")
    else:
        print("Sorry, we don't have " + requested_topping + "in storage.")
        
print("\nFinish making the pizza!")

