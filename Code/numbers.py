# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 20:22:57 2018

@author: Alicia
"""

#Numbers
a=2**3
print(a)

b=2+3*4
print(b)

c=2+3**4
print(c)

#Floats: python calls any number with a decimal point a float
d=0.2+0.1
print(d)

#get an arbitrary number of decimal places
print(repr(0.2+0.1))

#Avoiding type errors with the str()function
age=str(27)
message="happy " + age +"rd birthday."
print(message)

ageb=str(28)
print(age+" "+ageb)

print(int(age)+int(ageb))

#practice
aage=10
bage="20"
print(str(aage)+bage)

#the type of error called "cannot concatenate 'str' and 'int' objects" is 
d="20"
e=str(aage)+str(int(bage)+int(d))
print(e)

print(3/2)

#make sure that at least one of the numbers is a float
print(3.0/2)



