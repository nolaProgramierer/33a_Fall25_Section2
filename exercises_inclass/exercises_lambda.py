# A lambda is a small anonymous function. (function w/o a name)
# It can take any number of arguments, but have only one expression
# Useful whenever you want to create a function that's only a single line
# Use lambda functions with iterables like filter and map

# Syntax: lambda arguments: expression
# - 'lambda' is the keyword
# - 'arguments' are placeholders for inputs
# - 'expression' is the code that gets executed and returned

pianos = {
        "Steinway": 85000, 
        "Bechstein": 95000, 
        "Steingräber": 105000, 
        "Rönisch": 65000, 
        "Blüthner": 92000
}

#----------------------------------------------
print("1)")
# Regular function
def add_ten(num):
    return num + 10
print(add_ten(10))

#-----------------------------------------------
print()
print("2)")
# Lambda equivalent


#-----------------------------------------------
print()
print("3)")
# No function variable


#-----------------------------------------------
print()
print("4)")
# 3 arguments but only 1 expression that is evaluated



print()
print("5)")
# 5) Find the most expensive piano using a lambda


