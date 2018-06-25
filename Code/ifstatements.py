# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:55:28 2018

@author: Alicia
"""

car = 'audi'
print(car == 'volvo')

#checking multiple conditions
age_0=22
age_1=23
print(age_0>=21 and age_1>=21)

age_1=22
print(age_0>=21 and age_1>=21)

#Using or to Check Multiple Conditions
age_0=22
age_1=18
print(age_0>=21 or age_1>=21)

age_0=18
print(age_0>=21 or age_1>=21)

#Checking Whether a Value Is in a List
requested_toppings=['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('asd' in requested_toppings)

#Checking Whether a Value Is Not in a List
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish!")

#boolean expressions
game_active = True
can_edit = False

car = 'volvo'
print("Is car == 'volvo'? I predict True. ")
print(car=='volvo')

print("Is car == 'audi'? I predict False. ")
print(car=='audi')

age = 20
if age >= 19:
    print("You are an adult now!")
    print("Have you registered to vote?")
else:
    print("You are under age!")
    print("Wait!")

#The if-elif-else Chain
age = 18
if age < 4:
    print("\nYour admission cost is $0." )
elif age <18:
    print("\nYour admission cost is $10.")
else:
    print("\nYour admission cost is $100.")
    
age = 12
if age<4:
    price=0
elif age<18:
    price=10
else:
    price=100
print("\nyour admission cost is $" + str(price) + "!")

#Page 85
#Review page 53 For loop
magicians = ['a', 'b', 'c', 'alicia']
for magician in magicians: #we define a for loop. This line tells Python to pull a name from the list
#magicians, and store it in the variable magician.
    print(magician) 
print(magician.title() + ", that was a great trick!")
    