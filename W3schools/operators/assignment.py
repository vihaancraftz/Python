# assignment operato
# Assignment operators are used to assign values to variables:

# the walrus operator
## Python 3.8 introduced the := operator, known as the "walrus operator". It assigns values to variables as part of a larger expression:

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")