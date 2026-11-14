#Ternary operator
## The ternary operator allows you to assign one value if a condition is true, and another if it is false:

num = 6

x = "WEEKEND!" if num > 5 else "Workday"

print(x)

# the variable(x) is assigned to "weekend"
#num = 6 so if num is less than 5 it is considered a workday

#Instead of elif
#The ternary operator can be used instead of elif in longer if statements:

num = 6

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

print(x)