# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 21:46:07 2018

@author: Alicia
"""

#Review: define a class of dog that can later be used to build instances of any dog.
# Those two pieces of information (name and age) and 
# those two behaviors (sit and roll over) will go in our Dog class 
# because they’re common to most dogs.
class Dog():
    """A simple attmpt to model any dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name=name
        self.age=age
       
    def sit(self):
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        print(self.name.title() + " rolled over!")

# Making an Instance from a Class
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
      
# Accessing Attributes
print(my_dog.name)

# Calling Methods
my_dog.sit()
my_dog.roll_over()

# Try it yourself
class Restaurant():
    def __init__(self, name, cuisine):
        self.name=name
        self.cuisine=cuisine
        
    def describe_restaurant(self):
        print("Our restaurant is called: " + self.name.title() + " with " + 
              self.cuisine + " types os cuisines.")
        
    def open_restaurant(self):
        print("The status of our restaurant is open! ")

restaurant=Restaurant('deli', 5)
print(restaurant.name.title())
restaurant.open_restaurant()

# Setting a Default Value for an Attribute
class Car():
  """A simple attempt to represent a car."""
  def __init__(self, make, model, year):
    """Initialize attributes to describe a car."""
    self.make = make
    self.model = model
    self.year = year
  
  def get_descriptive_name(self):
    """Return a neatly formatted descriptive name."""
    long_name = str(self.year) + ' ' + self.make + ' ' + self.model
    return long_name.title()
   
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
        
class Car():
  def __init__(self, make, model, year):
     """Initialize attributes to describe a car."""
     self.make = make
     self.model = model
     self.year = year
     self.odometer_reading = 0
     
  def get_descriptive_name(self):
     """Return a neatly formatted descriptive name."""
     long_name = str(self.year) + ' ' + self.make + ' ' + self.model
     return long_name.title()

  def read_odometer(self):
     """Print a statement showing the car's mileage."""
     print("This car has " + str(self.odometer_reading) + " miles on it.")
  
# Modifying an Attribute’s Value Through a Method
  def update_odometer(self, mileage):
     """Set the odometer reading to the given value."""
     self.odometer_reading = mileage
     
  def increment_odometer(self, miles):
     """Add the given amount to the odometer reading."""
     self.odometer_reading += miles 

# Incrementing an Attribute’s Value Through a Method   
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
     
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23 # Modifying an Attribute’s Value Directly
my_new_car.read_odometer()


# Modifying an Attribute’s Value Through a Method
my_new_car.update_odometer(25)
my_new_car.read_odometer()

# page 172