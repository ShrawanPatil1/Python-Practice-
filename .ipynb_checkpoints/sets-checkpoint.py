# Sets :- { },   empty set :- set()

# EXAMPLE

""" METHOD OF SETS
add        # for adding new value
update      # for adding multipal values


"""
# Create an empty set.
set = {""}
print(set)

# Create a set containing 10, 20, 30, 40.

set1 = {"10", "20", "30", "40"}
print(set1)

# Add 50 to the set {10, 20, 30, 40}.
set2 = {"10", "20", "30", "40"}
set2.add("50")
print(set2)

# Add "Python" to the set {"Java", "SQL"}.
set3 = {"Java", "SQL"}
set3.add("Python")
print(set3)

# Add multiple elements 4, 5, 6 to the set {1, 2, 3}.
set4 = {"1", "2", "3"}
set4.update("4", "5", "6")
print(set4)

# Add "Mango" and "Orange" to the set {"Apple", "Banana"}.
set5 = {"Apple", "Banana"}
set6 ={"Mango", "Orange"}
print(set5 | set6)

# Remove 20 from the set {10, 20, 30, 40}.
# Remove "Python" from the set {"Java", "Python", "C++"}.
# Remove an element from the set {100, 200, 300, 400}.
# Remove all elements from the set {1, 2, 3, 4, 5}.
# Create an empty set and add 10, 20, 30 to it.
# Create a set with "Red" and "Blue" and add "Green" and "Yellow" to it.
# Create a set with 1, 2, 3, 4, 5 and remove 3 from it.
# Create a set with "Python", "SQL", "Excel" and remove "SQL" from it.
# Create a set with 100, 200, 300 and remove one element from it.
# Create a set with 1, 2, 3, 4 and remove all elements from it.
# Create a set with 10, 20 and add 30, 40 to it.
# Create an empty set and add "Apple", "Banana", "Mango" to it.
# Create a set with 10, 20, 30 and add 40, 50, 60 to it.

fruits = set()
fruits.update(["Apple", "Banana", "Mango"])
print(fruits)
