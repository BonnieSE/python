# -*- coding: utf-8 -*-
"""
Created on Mon Jul 09 21:22:14 2018

@author: Alicia
"""

# Passing an Arbitrary Number of Arguments
def make_pizza(*toppings):
   """Print the list of toppings that have been requested."""
   print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
  """Summarize the pizza we are about to make."""
  print("\nMaking a pizza with the following toppings:")
  for topping in toppings:
    print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):
  """Summarize the pizza we are about to make."""
  print("\nMaking a " + str(size) +
  "-inch pizza with the following toppings:")
  for topping in toppings:
    print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using Arbitrary Keyword Arguments
def build_profile(first, last, gender, **user_info):
    """Build a dictinary contains everything we know about a user."""
    profile = {}
    profile['first_name']=first
    profile['last_name']=last
    profile['Gender']=gender
    for key, value in user_info.items():
        profile[key] = value
    return profile
    
user_profile = build_profile('albert', 'einstein', 'girl',loction='princeton', field='physics')
print(user_profile)
# Page 154
