# abs()

# integer
integer = -20
print(f'absolute value of {integer}: abs({integer}) => {abs(integer)}')

# floating value
floating = -10.20
print(f'absolute value of {floating}: abs({floating}) => {abs(floating)}')

print(
    '''The python all() function accepts an iterable object (such as list, dictionary, etc.). 
    It returns true if all items in passed iterable are true. Otherwise, it returns False. 
    If the iterable object is empty, the all() function returns True.''')
# all values true
k = [1, 2, 3]
print(all(k))

k = [0, False]
print(f'{k} => all({k}) = {all(k)}')

# one false value
k = [1, 3, 7, 0]
print(all(k))

# one true value
k = [0, False, 5]
print(all(k))

# empty iterable
k = []
print(all(k))

print('''The python bin() function is used to return the binary representation of a specified integer. 
A result always starts with the prefix 0b.''')

x = 10
y = bin(x)

print(f'binary value of {x} is {y}')

# bool()
test1 = []
print(f'{test1} is {bool(test1)}')

test1 = [0]
print(f'{test1} is {bool(test1)}')

test1 = 0.0
print(f'{test1} is {bool(test1)}')

test1 = None
print(f'{test1} is {bool(test1)}')

test1 = True
print(f'{test1} is {bool(test1)}')

test1 = 'Easy String'
print(f'{test1} is {bool(test1)}')

# byte()
print('''The python bytes() in Python is used for returning a bytes object. 
It is an immutable version of the bytearray() function.

It can create empty bytes object of the specified size.''')
string = 'Hello World'
stringArray = bytes(string, 'utf-8')

print(f'{string}: {stringArray}')

print('''A python callable() function in Python is something that can be called. This build-in function checks and returns
true if the object passed appears to be callable otherwise false''')

x = 8
print(callable(x))

# compile()

print('''The python compile() function takes source code as input and 
returns a code object which can be executed later by exec() function''')

code_str = 'x=5\ny=10\nprint("sum = ", x+y)'
code = compile(code_str, 'sum.py', 'exec')

print(type(code))
exec(code)
#exec(x)

# ascii
# The python ascii() function returns a string containing a printable representation of an object and escapes the non-
# ASCII characters in the string using \x, \u or \U escapes.''')
normalText = 'Python is interesting'
print(ascii(normalText))

otherText = 'Pythön is interesting'
print(ascii(otherText))

print('Pyth\xf6n is interesting')

# bytearray()
normalText = 'Python is a programming language'

# string with encoding utf-8
arr = bytearray(string, 'utf-8')
print(arr)

# eval()
print('''The python eval() function parses the expression passed to it and runs python expression(code) within the 
program.''')

x = 9
print(eval('x + 1'))








