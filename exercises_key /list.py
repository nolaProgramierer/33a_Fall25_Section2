a = [1, 2, 3]
b = [4, 5, 6]

composers = [
            "Beethoven", "Ravel", "Brahms", "Debussy", 
            "Mahler", "Bruckner", "Mozart", 
            "Bach", "Stravinsky", "Chopin"
            ]

num_list = [1, 2, 3, 4, 5, 6, 7]

cars = [
    {"brand": "BMW", "trim": "328i", "color": "gray", "price": 38900},
     {"brand": "Mercedes", "trim": "350E", "color": "white", "price": 89000},
      {"brand": "Porsche", "trim": "911", "color": "orange", "price": 95000},
       {"brand": "Kia", "trim": "Sorento", "color": "blue", "price": 30900},
        {"brand": "Toyota", "trim": "Sienna", "color": "gray", "price": 51200},
    ]
# ---------------------------------------------------------------------------------#
print()
print("Exercise 1")
# 1) Instantiate a list of 3 piano brands 2 different ways (doesn't have to be pianos)
my_faves = list(("Steinway","Bösendorfer", "Bechstein"))
my_faves1 =["Steinway","Bösendorfer", "Bechstein"]
print(my_faves)
print(my_faves1)


print()
print("Exercise 2")
# 2) Find length of composers list
l = len(composers)
print(l)


print()
print("Exercise 3")
# 3) Concatenate list a and list b
c = a + b
print(c)


print()
print("Exercise 4")
# 4) Add 'Baldwin' to a 'myfaves' list
my_faves.append("Baldwin")
print(my_faves)


print()
print("Exercise 5")
# 5) Slice
# It is a technique used to extract a portion of a sequence, such as a list, 
# tuple, or string. Slices are created by specifying a start (inclusive), stop ()
# (exclusive), and optional step value within square brackets, 
# separated by colons (:). 
# e.g. [start:stop:step]

# a) Return a list [2, 3, 4]
l0 = num_list[1:4]
print(l0)

# b) Return a list [1, 2, 3]
l1 = num_list[:3]
print(l1)

# c) Return a list[5, 6, 7]
l2 = num_list[4:]
print(l2)

# d) Return a list [7, 6, 5, 4, 3, 2, 1]
l3 = num_list[::-1]
print(l3)


print()
print("Exercise 6")
# Traverse the composer list and print them to the screen
def list_composers(l):
    for item in l:
        print(item)

list_composers(composers)


print()
print("Exercise 7")
# 8) Return a list of car objects
def show_objs(objArr):
    for obj in objArr:
        print(obj)

show_objs(cars)


print()
print("Exercise 8")
# 9) Return a list of the composers that begin with the letter 'B'
def composers_starts_with(comps, letter="B"):
    result = []
    for comp in comps:
        if comp.startswith(letter):
            result.append(comp)
    return result

filtered_composers = composers_starts_with(composers)
print(filtered_composers)






