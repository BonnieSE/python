# large files
filename = 'pi_digits.txt'
with open(filename) as file_object:
   lines = file_object.readlines()
pi_string = ''
for line in lines:
   pi_string += line.strip()
print(pi_string[:20])
print(len(pi_string))

filename = 'pi_digits.txt'
with open(filename) as file_object:
   lines = file_object.readlines()

pi_string = ''
for line in lines:
   pi_string += line.rstrip()
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
   print("Your birthday appears in the first million digits of pi!")
else:
   print("Your birthday does not appear in the first million digits of pi.")

# Try it yourself
filename = 'learning_python.txt'
with open(filename) as file_object:
   contents = file_object.read()
   print(contents)

filename = 'learning_python.txt'
with open(filename) as file_object:
    for line in file_object:
       print(line)

filename = 'learning_python.txt'
with open(filename) as file_object:
   lines = file_object.readlines()

for line in lines:
    print(line)

message = 'I like you'
it=message.replace('you','him')
print(it)

print('I like you'.replace('you','him'))

print('Hello world'.replace('world', 'Guido'))

filename = 'learning_python.txt'
with open(filename) as file_object:
   lines = file_object.readlines()

for line in lines:
    it=line.replace('python','C')
    print(it)
