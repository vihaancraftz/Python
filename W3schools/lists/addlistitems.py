# add list items

#append items
#To add an item to the end of the list, use the append() method:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#insert items
# to insert a list item at a specified index, use the insert() method.
# the insert() method inserts an item at the specified index:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#extended list
#to append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#add any iterable
# the extend() method does not hace to append lists, you can add any iterable object(tuples, sets, dictionaries etc.).

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

