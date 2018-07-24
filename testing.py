from name_function import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
       break
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')

# A Passing Test
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()

# Responding to a Failed Test
def get_formatted_name(first, last, middle=''):
  """Generate a neatly formatted full name."""
  if middle:
    full_name = first + ' ' + middle + ' ' + last
  else:
    full_name = first + ' ' + last
  return full_name.title()
