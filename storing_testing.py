import json
number = [2, 3, 5, 7, 11, 13]
filename = 'number.json'
with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)

# Uses json.load() to read the list back into memory:
import json

filename = 'number.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)

# Saving and Reading User-Generated Data
username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We use cookies, " + username)

file = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username)
else:
    print("Wecome back, " + username)

# Refactoring
def greet_user():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
    else:
            print("Welcome back, " + username + "!")
greet_user()

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = input("What is your name?")
        filename = 'username.json'
        with open(filename,'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username)
greet_user()