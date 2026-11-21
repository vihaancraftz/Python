# change list items

#change ltem value
#To change the value of a specific item, refer to the index number:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change a Range of Item Values
#To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:\

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# insert items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)