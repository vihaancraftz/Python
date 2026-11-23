# list comprehension
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#Example:

#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

#Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


# the syntax
newlist = [expression for item in iterable if condition == True]
# the return value is a new list, leaving the old list unchanged.

#condition
#the condition is like a filter that only accepts the items that evaluate to True.
newlist = [x for x in fruits if x !="apple"]

#with no if statement:
newlist = [x for x in fruits]

#iterable
# the iterable can be any iterable object, like a list, tuple, set etc.

newlist = [x for x in range(10)]

#expression
#expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends ip like a list item in the new list:

newlist = [x.upper() for x in fruits]