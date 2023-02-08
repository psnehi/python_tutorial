# format()
# d, f and b are a type
# integer
print('integer', format(123, "d"))
print('float', format(123.456789, "f"))
print('binary', format(12, "b"))

# frozenset
# tuple of letters
letters = ('a', 'e', 'i', 'o', 'u')
fset_forzenset = frozenset(letters)
print(f'frozenset of tuple {letters}: {fset_forzenset}')
print(f'empty frozenset is: {frozenset()}')

# getattr() the python getattr() function returns the value of a named attribute of an object. if it is not found,
# it returns the default value

print('getattr()')


class Details:
    age = 22
    name = 'Phill'


details = Details()
print(f'The age is: {getattr(details, "age")}')
print(f'The age is: {details.age}')

print("""
# globals()
# it returns the dictionary of hte current global symbol table
# a Symbol table is defined as a data structure which contains all the necessary information about the program. It includes 
variable names, methods, classes, etc. """)

age = 22
globals()['age'] = 30
print(age)


print("""
The python iter() function is used to return an iterator object. It creates an object which can be iterated one element 
at a time. Python iter() Function Example """)

# list of numbers
list = [1, 2, 3, 4, 5]

listIter = iter(list)

# prints '1'
print(next(listIter))

# list()
print("""list() function creates a list""")
string = 'Prashant'
print(f'string: {string} converts to list using list(string): {list(string)}')

tuples = (1, 2, 3, 4, 5)
print(f'tuple: {tuples} converts to list using list(string): {list(tuples)}')

# prints '2'
print(next(listIter))

# prints '3'
print(next(listIter))

# prints '4'
print(next(listIter))

# prints '5'
print(next(listIter))


