# Identity operators
## identity operators are used to compare the objects, ot if they are equal, but if they are actually the same object, with the same memory location:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

# Difference between is and ==
#is - Checks if both variables point to the same object in memory
#== - Checks if the values of both variables are equal

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)