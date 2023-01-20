# Example Python Code for Pass by Reference vs. Value
# defining the function
def list_square_function(item_list):
    """This function will find the square of items in the list"""
    squares = []
    for item in item_list:
        squares.append(item ** 2)
    return squares


print(list_square_function.__doc__)
my_list = [2, 4, 6]
print(
    f'list_square_function(item_list) will return Squares of each items in list: {my_list}: {list_square_function(my_list)}')


# Python code to demonstrate the use of keyword arguments
# Defining a function
def function(n1, n2):
    print("number 1 is: ", n1)
    print("number 2 is: ", n2)


# Calling function and passing arguments without using keyword
print("Without using keyword")
function(50, 30)

# Calling function and passing arguments using keyword
print("With using keyword")
function(n2=50, n1=30)


# Python code to demonstrate the use of default arguments
# Defining a function
def function(n1, n2):
    print("number 1 is: ", n1)
    print("number 2 is: ", n2)


# Calling function and passing two arguments out of order, we need num1 to be 20 and num2 to be 30
print("Passing out of order arguments")
function(30, 20)

# Calling function and passing only one argument
print("Passing only one argument")
try:
    function(30)
except:
    print("Function needs two positional arguments")

print('*****************************************************************')
print('# Python code to demonstrate the use of variable-length arguments')

print("*args -These are Non-Keyword Arguments\n"
      "**kwargs -These are Keyword Arguments.")


# Defining a function
def function(*args_list):
    ans = []
    for i in args_list:
        ans.append(i.upper())
    return ans


print('# Passing args arguments')
obj = function('python', 'asp.net', 'tutorial')
print(obj)


# defining a function
def function(**kargs_list):
    ans = []
    for key, value in kargs_list.items():
        ans.append([key, value])
    return ans


# Passing kwargs arguments
obj = function(First="Python", Second="Functions", Third="Tutorial")
print(obj)


# Python code to demonstrate the use of return statements
# Defining a function with return statement
def square(num):
    return num ** 2


print(f'Function with return statement: {square(10)}')


def square(num):
    num = num ** 2


print(f'Function without return statement: {square(10)}')
