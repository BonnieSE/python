# Handling the FileNotFoundError Exception

filename = 'alice.txt'
try:
   with open(filename) as f_obj:
     contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " doesn't exist."
    print(msg)

# Analyzing Text
title = "Harry;Potter;hi;"
it=title.split(';')
print(it)
a,b,c = title.split(';', maxsplit=2)
print(b)

filename = 'alice.txt'
with open(filename, 'w') as file_object:
    file_object.write("Programming is a necessary skill.")
    file_object.write("\nProgramming is a necessary skill.")

filename = 'alice.txt'
try:
  with open(filename) as f_obj:
    contents = f_obj.read()
except FileNotFoundError:
  msg = "Sorry, the file " + filename + " does not exist."
  print(msg)
else:
    # Count the approximate number of words in the file.
   words = contents.split()
   num_words = len(words)
   print("The file" + filename + " has about " + str(num_words) + " words.")
   print(words)

# Working with Multiple Files
def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, " + "the file: " + filename + " doesn't exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'learning_python.txt']
for filename in filenames:
  count_words(filename)

# Failing Silently
def count_words(filename):
    try:
        with open(filename) as f_obj:
          """open a file, process its contents, and make sure to close it"""
          contents = f_obj.read()
    except FileNotFoundError:
        pass  #Failing silently!
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'learning_python.txt']
for filename in filenames:
  count_words(filename)

# Try it yourself!

# Storing Data
import json
numbers = [2, 3, 5, 12]
filename = 'number.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, name, model, year, color):
        self.name = name
        self.model = model
        self.year = year
        self.color = color

    def get_new_car(self):
        print("My new car is a " + str(self.name) + str(self.model) + str(self.year) + "with the color: " + str(self.color) + ".")

my_car = Car('Volvo', 'V60', '2010', 'blue')

filename2 = 'my_car.json'
with open(filename2, 'w') as c:
    json.dump(my_car.__dict__, c)

# Using json.dump() and json.load()
# Page 209




