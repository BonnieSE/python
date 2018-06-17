# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 09:38:34 2018

@author: Alicia
"""

# Adding Whitespace to Strings with Tabs or Newlines

print("    python")
print("\tpython")
print("languages:\nPython\t*\nC\nJava")

message = "languages:\n\tpython\n\tC"
print(message.title())
print(message.upper())

favor_language = 'python '
print(favor_language)

favor_language = favor_language.rstrip()
print(favor_language)

str1='python '
str2='python'

#str1 have an extra space right side, compare it with str2
print(str1==str2)  #False
print(str1.rstrip() == str2)  #True

str1=' python'

#str1 have an extra space left side, compare it with str2
print(str1==str2)  #false
print(str2==str1.lstrip())  #true

str1=' python '
#str1 have 2 extra spaces both sides, compare it with str2
print(str1==str2)  #false
print(str1.strip()==str2)  #true

# Avoiding Syntax Errors with Strings
word = "emanate's meaning is to come out from a source."
print(word)

# However, if you use single quotes, Python can’t identify where the string
# should end
word = 'emanate\'s meaning is to come out from a source.'
print(word)

print"åöä"
