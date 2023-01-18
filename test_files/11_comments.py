# single line comment
# This code is to show an example of single line comment
print("This statement is not have a hashtag before it")

print("This is not a comment ")  # this code is to show example of single line comment

# multiline comment
'it is a comment extending to multiple line'
'if any string is not assigned to any variable it will be commented out'


# python doc string
def add(x, y):
    """This function adds the value of two input variables"""
    return x + y


print(f'Calling add function: {add(7, 9)}')
# displaying the docstrings of the add function
print(add.__doc__)

