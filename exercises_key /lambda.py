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
x = lambda a : a + 10
print(x(10))

#-----------------------------------------------
print()
print("3)")
# No function variable
z = (lambda x: x + 10)(10)
print(z)

#-----------------------------------------------
print()
print("4)")
# 3 arguments but only 1 expression that is evaluated
y = lambda a, b, c : a + b + c
print(y(1, 2, 3))


print()
print("5)")
# 5) Find the most expensive piano using a lambda
most_valuable_piano = max(pianos, key=lambda k: pianos.get(k))
print(f"Most valuable piano: {most_valuable_piano}")


#-------------------------------------------------------------------

print()
print("6)")
# Sort by price (dictionary values)

# How sorted() works:
# 1. pianos.items() returns a list of (brand, price) tuples.
# 2. The lambda function extracts the price (x[1]) from each tuple.
# 3. sorted() orders the list based on price (ascending by default).
sorted_pianos = sorted(pianos.items(), key=lambda x: x[1])
print(sorted_pianos)


print()
print("7)")
# Return a list of pianos over 94000 with filter and a lambda

# How filter() works:
# 1. filter() applies the lambda to each piano brand (key in the dictionary).
# 2. The lambda checks if the price (pianos[x]) is over 94,000.
# 3. filter() returns only the brands that meet the condition.

expensive_pianos = list(filter(lambda x: pianos[x] > 94000, pianos))
print(expensive_pianos)


print()
print("8)")
# How map() works:
# 1. map() applies the lambda function to each car in the dictionary.
# 2. The lambda calculates the new price: (price * 0.15) + price.
# 3. map() returns a list of formatted prices.

# Using map return a list of car prices with a price increase of 15%
cars = {"Ford": 25000, "Chevy": 35000, "Dodge": 37500}

newPrice = list(map(lambda k: f"${(cars[k] * .15) + cars[k]:.2f}", cars))
print(newPrice)



print()
most_expensive_piano = max(pianos, key=pianos.get)
print(most_expensive_piano)
print(pianos[most_expensive_piano])

most_expensive_piano_info = max(pianos.items(), key=lambda k: k[1])
print(most_expensive_piano_info)



