# Tuples
# A tuple is sequence of values, of any type, that are immutable
# Tuples are written with round brackets.
# Immutability, faster that lists, multiple return values, 
# protect data from modification

print("1)")
# Instantiate a tuple
t0 = 'a', 'b', 'c', 'd', 'e'
print(t0)


print()
print("2)")
# Instantiate a tuple
t1 = ('a', 'b', 'c', 'd', 'e')
print(t1)


print()
print("3)")
# Swap values without a temporary variable
a, b = 5, 10
a, b = b, a
print(a, b)


print()
print("4)")
# Tuples are hashable, and as such can be used as dictionary keys

location_data = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles"
}

print(location_data[(40.7128, -74.0060)])  # Output: New York









  