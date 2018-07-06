# -*- coding: utf-8 -*-
"""
Created on Fri Jul 06 21:34:02 2018

@author: Alicia
"""

message = input("Tell me sth. and I will repeat it to you: ")
print(message)

name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "if you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print("\nHello, " + name + "!")

#Using int() to Accept Numerical Input
age = input("How old are you? ")
age = int(age)
print(age >= 18)

height = input("How tall are you, in inches? ")
height = int(height)

if height >=36:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou come back when you're a little older.")
 
#The Modulo Operator
print(4 % 3) #it just tells you what the remainder is.
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

#Introducing while Loops
    current_number = 1
    while current_number <=5:
        print(current_number)
        current_number += 1
        
#Letting the user choose when to quit
prompt = "\nTell me something, and I will repeat it back to you: "
prompt +="\nEnter 'quit' to end the program. "
message = ""
# to store whatever value the user enters. 
# We define message as an empty string, "".
while message != 'quit':
# This while loop w runs as long as the value of message is not 'quit'.
  message = input(prompt)
  print(message)
  
active = True #Page 125
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)
    

  



    


