##Boolean Values
#In programming you often need to know if an expression is True or False.

#You can evaluate any expression in Python, and get one of two answers, True or False.

#When you compare two values, the expression is evaluated and Python returns the Boolean answer:

print(10 > 9)
print(10 == 9)
print(10 < 9)

#evaluate values and variables
print(bool("Hello"))
print(bool(15))

#most values are true
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


#some values are false]
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#functions can return as a boolean
def myFunction() :
  return True

print(myFunction())

