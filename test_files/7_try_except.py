# initilize the number
var1 = 4
var2 = 0

# Exception raised in try section
try:
    d = var1 // var2  # this will raise a "divide by zero exception"
    print(d)

# this section will handle exception raised in try block
except ZeroDivisionError:
    print("We can't divide by zero")
finally:
    # if exception raised or not, this block will be executed every time
    print("This is inside finally block")

# by using assert keyword we will check if var2 is 0
print("The value of var1 / var2 is: ")
assert var2 != 0, "Divide by 0 error"
print(var1 / var2)
