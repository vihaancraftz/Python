## strings

# Strings in Python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# you can display a string literal with the print() function:

print("Hello")
print('Hello')

# quotes inside quotes
# you can use quotes inside a string, as long as they do not match the quotes surrounding

print("It's alright.")
print('He said "Hello".')

#assign string to a variable
a = "Hello"
print(a)

## multiline strings
a = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""
print(a)
#or 3 single quotes
a = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'''
print(a)

# strings are arrays
a = "Hello, World!"
print(a[1])

## looping through a string
for x in "banana":
  print(x)

# string length
a = "Hello, World!"
print(len(a))

## check string
txt = "The best things in life are free!"
print("free" in txt)
#use it in an if statement
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)
#use it in an if statement
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")