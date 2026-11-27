# sort list
#list objects have a sort() method that will sort the list alphanumerically, ascending, by default:

#sort list alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple"]
thislist.sor
print(thislist)

#sort descending
#to sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple"]
thislist.sort(reverse = True)
print(thislist)

#customize sort function
#you can also customize your own function by using the keyword argument key = function.
#The function will return a number that will be used to sort the list (the lowest number
def myfunc(n):
    return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#case insensitive sort
#by default the sort() method is case sensitive, resulting in all capital letters being sorted before
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower, reverse = True)
print(thislist)