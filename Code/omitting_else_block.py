# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 21:35:27 2018

@author: Alicia
"""

#Omitting the else Block
age = 17
price = 0
if age < 4:
    price = 0
elif age < 18:
    price=5
elif age < 65:
    price=10
elif age < 65:
    price=5
elif age > 85:
    price=0

print("Your cost is: " + str(price) + ".") #Why the price must be string?

#Testing multople conditions
requested_skills = ['SQL', 'ETL']

if 'SQL' in requested_skills:
    print("Learn SQL.")
if 'ETL' in requested_skills:
    print("Learn ETL.")
if 'a' not in requested_skills:
    print("a not in skills list.")

print("\nFinished making your plan!")

age = 17
if age < 2:
    print("The person is a baby.")
if age >= 2 and age < 4:
    print("The person is a toddler.")
elif age >= 4 and age < 13:
    print("The person is a kid.")
if age >=13 and age < 20:
    print("The person is a teenager.")
if age >=20 and age < 65:
    print("The person is an adult.")
    
#Using if statements with lists(if statements + for loop)
requested_skills = ['SQL', 'ETL', 'tableau']
for requested_skill in requested_skills:
  if requested_skill == 'SQL':
    print("Sorry, lacking study resources for SQL right now!")
  else:
    print("Please start your study journey!")
    print("Learning" + requested_skill + ".")

print("\n\tStudy hard on " + requested_skill + "!") #Why here will present the "tableau"? Because of the for loop processing order.

#Checking that a list is not empty
requested_toppings = ['']
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#Page91
    