# This python file has python style errors


import datetime, date  # Import multiple unrelated modules

# Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Habitant morbi tristique senectus et. Felis eget velit aliquet sagittis id consectetur.

def some_function():
print("Hi there!")      # Indentation error
                        # Should have 2 lines after class or function definition
def foo(a,b,c):         # Spacing after commas
   x = a * c     
   y =b * c             # Missing space
   if (x+y)> 400:       # Space around operators
      print("It's greater than 400!")
   elif (x+y) < 400:    # Space around operators
      print("It's less than 400")
   else:
      print("It's 400")
                        # Missing line
   foo(3, 2, 2)         # Over indented

def bar(x, y):
   return x + y

dict = {'key1': 'value1', "key2": "value2", 'key3': 2001}   # Mixed quoting
dict['key1'] = dict ['hello']      # Space after right hand assignment

