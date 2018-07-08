# -*- coding: utf-8 -*-
"""
Created on Sun Jul 08 20:55:31 2018

@author: Alicia
"""

# Returning a Dictionary
def build_person(first, last):
    """Return a dictionary of info about a person."""
    person = {'f': first, 'l': last}
    return person
    
musician = build_person('jimmy', 'Brown')
print(musician)

def biuld_person(first_name, last_name, age=''):
    """Return a dictionary of info about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
    
musician = biuld_person('jimmy','brown')
print(musician)

# Using a Function with a while Loop---Page 145
#def get_formatted_name(first_name, last_name):
#  """Return a full name, neatly formatted."""
#   full_name = first_name + ' ' + last_name
#   return full_name.title()
# This is an infinite loop!
#while True:
#   print("\nPlease tell me your name:")
#  f_name = input("First name: ")
#   l_name = input("Last name: ")
#  formatted_name = get_formatted_name(f_name, l_name)
#   print("\nHello, " + formatted_name + "!")
   
# Passing a List
def greet_users(names):
  """Print a simple greeting to each user in the list."""
  for name in names:
    msg = "Hello, " + name.title() + "!"
    print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
   
# Modifying a List in a Function
# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendent', 'dodecahedron']
completed_models = []

#simulate printing each design, until none are left
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design=unprinted_designs.pop()
#Simulate creating a 3D print from the design
    print("printing model " + current_design)
    completed_models.append(current_design)
    
# Display all completed models
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)
