# -*- coding: utf-8 -*-
"""
Created on Sun Jul 01 20:14:31 2018

@author: Alicia
"""

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'yellow', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
#Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

#show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))
for alien in aliens[0:3]:
    if alien['color']=='green':
       alien['color'] = 'yellow'
       alien['points'] = 10
       alien['speed'] = 'medium'
    elif alien['color']=='yellow':
       alien['color']='red'
       alien['points']=15
       alien['speed']='fast'
    
#show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
    
#A list in a dictionary
#Sotre info about a pizza being ordered
pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese', 'onion', 'tomato'],
         }
#Summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
for topping in pizza['toppings']:
    print("\t\n" + topping)
    
    favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items(): #P112--P103
#the method items(), which returns a list of key-value pairs.
  print("\n" + name.title() + "'s favorite languages are:")
  for language in languages:
    print("\t" + language.title())

#A dictionary in a dictionary
  users = {
    'aeinsein': {
        'first': 'albert',
        'last': 'einsein',
        'location': 'princeton',
                 },
    'mcurie':   {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
                 },         
           }
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
