# literals

x = 0b10100  # Binary Literals
y = 100  # Decimal Literal
z = 0o215  # Octal Literal
u = 0x12d  # Hexadecimal Literal

# Float Literal
float_1 = 100.5
float_2 = 1.5e2

# Complex Literal
a = 5 + 3.14j

print(f'Binary: {x}, Decimal: {y}, Octal: {z}, Hexadecimal: {u}')
print(f'Float: {float_1}, Float: {float_2}')
print(f'Complex Literal {a}, {a.imag}, {a.real}')

# list
list_ = ['John', 678, 20.4, 'Peter']
list_1 = [456, 'Andrew']
print(f'Example of list: {list_}')
print(f'Addition of two lists: {list_ + list_1}')

# dictionary
dic = {'name': 'prashant', 'age': 18, 'roll_no': 31}
print(f'Example of dictionary is: {dic}')

# tuple
tup = (10, 20, 'Dev', [2, 3, 4])
print(f'Example of tuple is: {tup}')

# set: set is the collection of the unordered cataset, it is enclosed by {} and each element is seperated by comma(,)
set_example = {'apple', 'orange', 'guava', 'papaya'}
print(f'Example of set is: {set_example}')
