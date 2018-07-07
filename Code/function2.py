# -*- coding: utf-8 -*-
"""
Created on Sat Jul 07 15:58:20 2018

@author: Alicia
"""

# Order Matters in Positional Arguments
def describe_pet(animal_type, pet_name):
    """Display info about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet('er', 'hamster')

# Keyword arguments(The order of keyword arguments doesn’t matter 
# because Python knows where each value should go.)

def describe_pet(animal_type, pet_name):
    """Display info about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='harry', animal_type='hamster')

# Default Values
def describe_pet(pet_name, animal_type = 'dog'):
    """Display info about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('earl')

# Try it yourself
def make_shirt(size, text_sms):
    """Disply size and message on the shirt"""
    print("There's slogan on my shirt which wrote: " + text_sms + 
    " and the size of my shirt is " + size + ".")
make_shirt(size='21', text_sms='Fight!')

# Return Values
# Returning a Simple Value
def get_formatted_name(first, last):
    """return a full name, neatly formatted"""
    full_name = first + ' ' + last
    return full_name.title()
    
musician = get_formatted_name('Jimmy', 'Lee')
print(musician)

# Making an Argument Optional
def get_formatted_name(first, last, middle=''):
    """return a full name, neatly formatted"""
    if middle:
        full_name = first + ' ' + middle + ' ' +last
    else:
        full_name = first + ' ' +last
    return full_name.title()
    
musician = get_formatted_name("\n"+'Jimmy', 'Lee')
print(musician)

# Page 144
