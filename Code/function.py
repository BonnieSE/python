# -*- coding: utf-8 -*-
"""
Created on Thu Jul 05 21:34:38 2018

@author: Alicia
"""

#Functions: which are named blocks of code that are designed to do one specific job. 
#Defining a Function
def greet_user():
# the keyword def to inform Python that you’re defining a function.
# In this case, the name of the function is greet_user()
# it needs no information to do its job, so its parentheses are empty.
    """Display a simple greeting!"""
# it needs no information to do its job, so its parentheses are empty.
    print("Hello!")
# This line is the only line of actual code in the body of this function, 
# so greet_user() has just one job: print("Hello!")
greet_user()
# To call a function, you write the name of the function, 
# followed by any necessary information in parentheses,
# as shown here. Because no information is needed here, calling our
# function is as simple as entering greet_user().


#Passing Information to a Function
def greet_user(username): #username = a parameter in the function
    """Display a simple greeting"""
    print("Hello! Greet " +username.title())
greet_user('Fredrika') #Fredriks = an arguement, this value is stored in the parameter(username)

#Positional arguments
def describe_pet(animal_type, pet_name):
    """Display info about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + " 's name is " + pet_name.title() + "!")
describe_pet('cat', 'Zoey')

#Multiple function calss
describe_pet('dog', 'willie')
#Page 137

