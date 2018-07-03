# -*- coding: utf-8 -*-
"""
Created on Tue Jul 03 21:01:59 2018

@author: Alicia
"""

#Using continue in a Loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0 :
        continue
    print(current_number)
        
#Avoiding Infinite Loops
x=1
while x <= 5:
    print(x)
    x += 1

#Using a while Loop with Lists and Dictionaries
#Moving Items from One List to Another

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    
print("The following user have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
  pets.remove('cat')
  print(pets) 