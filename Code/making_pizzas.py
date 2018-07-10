# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 21:48:17 2018

@author: Alicia
"""

def make_pizza(size, *toppings):
   """Summarize the pizza we are about to make."""
   print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
   for topping in toppings:
       if size==12:
          print("The price is 10 with: " + topping)
       elif size==16:
          print("The price is 20 with: " + topping)
    