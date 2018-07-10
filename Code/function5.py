# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 20:16:04 2018

@author: Alicia
"""

import making_pizzas
  
making_pizzas.make_pizza(16, 'pepperoni')
making_pizzas.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to Give a Function an Alias
from making_pizzas import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

import making_pizzas as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from making_pizzas import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

def pizza(size, *toppings):
    """Return a price, according to size."""
    print(len(toppings))
    if size>=5 and size<10 and len(toppings)<2:
        price=35
    elif size<20:
        price=50
    return price
   
order=pizza(15, 'lax', 'tomato', 'shrimp')

print("\nThe price of your pizza is " + str(order))

