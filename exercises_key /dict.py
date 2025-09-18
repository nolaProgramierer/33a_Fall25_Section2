# List of car dictionaries
cars = [
    {"brand": "BMW", "trim": "328i", "color": "gray", "price": 38900},
    {"brand": "Mercedes", "trim": "350E", "color": "white", "price": 89000},
    {"brand": "Porsche", "trim": "911", "color": "orange", "price": 95000},
    {"brand": "Kia", "trim": "Sorento", "color": "blue", "price": 30900},
    {"brand": "Toyota", "trim": "Sienna", "color": "gray", "price": 51200},
]

# Piano dictionary
pianos = {
        "Steinway": 85000, 
        "Bechstein": 95000, 
        "Steingräber": 105000, 
        "Rönisch": 65000, 
        "Blüthner": 92000
        }


print("1)")
#------------------------------------------------------
# 1) List of piano brands (keys)
piano_brands = list(pianos.keys())
print(f"Piano brands: {piano_brands}")


print()
print("2)")
# 2) List of piano prices (values)
piano_prices = list(pianos.values())
print(f"Piano prices:", piano_prices)


print()
print("3)")
# 3) List of key-value tuples
piano_items = list(pianos.items())
print(f"Piano key-value pairs:", piano_items)


print()
print("5)")
# Return a list of piano values
piano_values = [v for k, v in pianos.items()]
print(piano_values)


print()
print("6)")
# Find cars that are less than $40000 (list comprehension)
cheap_cars = [car for car in cars if car["price"] < 40000]
print("Cheap cars:", cheap_cars)


print()
print("7)")
# Find orange car using 'get' method
# Using 'get' prevents a KeyError if a key:value pair doesn't exist
def find_orange_car(obj_list):
    return [car for car in obj_list if car.get("color") == "orange"]

print("Orange car:", find_orange_car(cars))


# ------------------------------------------------------------------------
print()
print("8)")
# Take 'cars' list and returns a list of all car brands
# def find_brands(car_dict):
#     car_list = []
#     for car in car_dict:
#         car_list.append(car.get("brand"))
#     return car_list


def find_brands(car_dict):
    return [car["brand"] for car in car_dict]

print(find_brands(cars))

print()
print("9)")
# Return a list of cars (whole dictionary entry) that have the color 'gray'

def find_gray_car(cars_dict):
    return [car for car in cars_dict if car.get("color") == "gray"]

print(find_gray_car(cars))


print()
print("10)")
# Write a function that finds and returns the dicionary of the most
# expensive car

def find_most_exp_car(cars_dict):
    return max(cars_dict, key=lambda x: x["price"])
    
print(find_most_exp_car(cars))



    



    
