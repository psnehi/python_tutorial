a = 1
b = 'a'
c = [1, 2, 3, 4, 5]
d = [1, 'prashant', 'snehi', 3]

print('Type of a: ', type(a))
print('Type of b: ', type(b))
print('Type of c: ', type(c))
print('Type of d: ', type(d))

# list slicing
print(c[3:])
print(c[0:2])

# list concatenate
print(c + d)
print(c * 2)

# tuple: are like list but enclosed with () and seperated by , Tuples are readonly data structure and can't be modified
tuples = (1, 2, 3, 4, 5)
print(f'Type of Tuples: {tuples} is {type(tuples)}')

# dictionary
dic = {1: 'Jimmy', 2: 'Alex', 3: 'John', 4: 'Mike'}
print(f'Type of dic {dic} is {type(dic)}')

print(f'First name is: {dic[1]} and second name is {dic[2]}')

print(f'Keys in dictionary {dic.keys()}')
print(f'Values in dictionary {dic.values()}')

# boolean
print(type(True)," ",  end="")
print(type(False))

'''Set: Python Set is the unordered collection of the data type. It is iterable, mutable(can modify after creation), 
and has unique elements. In set, the order of the elements is undefined; it may return the changed sequence of the 
element. The set is created by using a built-in function set(), or a sequence of elements is passed in the curly 
braces and separated by the comma. It can contain various types of values. Consider the following example.'''

# Creating Empty set
print('Set example')
set1 = set()

set2 = {'James', 2, 3, 'Python'}

# Printing Set value
print(set2)

# Adding element to the set

set2.add(10)
print(set2)

# Removing element from the set
set2.remove(2)
print(set2)

