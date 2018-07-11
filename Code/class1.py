# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 22:52:57 2018

@author: Alicia
"""

class Dog():
  """A simple attempt to model a dog."""
  def __init__(self, name, age):
     """Initialize name and age attributes."""
     self.name = name
     self.age = age
  def sit(self):
     """Simulate a dog sitting in response to a command."""
     print(self.name.title() + " is now sitting.")
  def roll_over(self):
     """Simulate rolling over in response to a command."""
     print(self.name.title() + " rolled over!")
     
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.name

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()