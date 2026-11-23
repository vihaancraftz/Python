#Loop lists

# loop through a list
#you can loop through the list items by using a for loop

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# loop through the index numbers
# you can also loop through the list items by reffering to their index number.
#use the range() and len() functions to create a suitable iterable.

thislist = ["apple", "banana", "cherry"]
for i in range (len(thislist)):
    print(thislist[i])

#using a while loop
# you can loop through the list items by using a while loop.
# use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
#remember to increase the indez by 1 after each iteration.

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# looping using list comprehension
#list comprehension offers the shortest syntax for looping thorugh lists:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]