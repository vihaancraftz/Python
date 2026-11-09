#String Format
#As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)
#But we can combine strings and numbers by using f-strings or the format() method!

#f-strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#placeholders and modifiers
price = 59
txt = f"The price is {price} dollars"
print(txt)


#