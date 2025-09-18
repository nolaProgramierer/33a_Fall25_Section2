# List comprehension

 # [expression for item in iterable (if condition)]
    # 1) expression: expresion to evaluate and append to the new list
    # 2) item: the variable representing each element in the iterable (e.g., a list, tuple, or string).
    # 3) iterable: the sequence or iterable to iterate over
    # 4) condition (optional): An expression to filter elements based on a condition.

# The expression is the current item in the iteration but also the outcome which can 
# be manipulated before it is added to the new list
# The condition is like a filter that only accepts the items that valuate to True.


print("1)")
# tuple!
composers = "Beethoven", "Ravel", "Debussy", "Rachmaninoff", "Chopin", "von Weber"

#Return a list of composers with a certain letter in the name
def composers_with_ltr(composers_tuple, ltr="v"):
    new_composers = []
    for composer in composers_tuple:
        if ltr in composer:
            new_composers.append(composer)
    print(new_composers)

composers_with_ltr(composers)


print()
print("2)")
# 2) Render the above function as a list comprehension
def composers_with_ltr_comp(comps, ltr="v"):
    result = [composer for composer in comps if ltr in composer]
    return result
print(composers_with_ltr_comp(composers))


print()
print("3)")
# 3) Return a list of tuples with the composer containing a 
#   certain letter along with the length of the composer's name
def composers_with_ltr_len(comp_seq, ltr="v"):
    result = [
            (composer.upper(), len(composer))
              for composer in comp_seq 
              if ltr in composer
              ]
    return result

print(composers_with_ltr_len(composers,"a"))








