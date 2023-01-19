# a simple list
list1 = [1, 2, "Python", "Program", 15.9]
list2 = ["Amy", "Ryan", "Henry", "Emma"]

# printing the list
print(list1)
print(list2)

# printing the type of list
print(type(list1))
print(type(list2))

'''
Characteristics of Lists
The list has the following characteristics:

The lists are ordered.
The element of the list can access by index.
The lists are the mutable type.
The lists are mutable types.
A list can store the number of various elements.
'''
print('ordered list checking')
print('*********************')
# example
a = [1, 2, 'Ram', 3.50, 'Rahul', 5, 6]
b = [1, 2, 5, 'Ram', 3.50, 'Rahul', 6]

print(f'Unidentical list: {a == b}')

x = [1, 2, 'Ram', 3.50, 'Rahul', 5, 6]
y = [1, 2, 'Ram', 3.50, 'Rahul', 5, 6]

print(f'Dentical List: {x == y}')

# list example in details
emp = ['John', 102, 'USA']
dept_1 = ['CS', 10]
dept_2 = ['IT', 11]
hod_cs = [10, 'Mr. Holding']
hod_it = [11, 'Mr. Bewon']
print("printing employee data")
print('Name: %s, Id: %d, Country: %s' % (emp[0], emp[1], emp[2]))

print('Printing Departments...')
print(
    'Department 1:\n Name: %s, Id: %d\nDepartment 2:\n Name: %s, Id: %d' % (dept_1[0], dept_1[1], dept_2[0], dept_2[1]))

print('HOD Details...')
print('CS HOD Name: %s, Id: %d,' % (hod_cs[1], hod_cs[0]))
print('IT HOD Name: %s, Id: %d,' % (hod_it[1], hod_it[0]))

print("Lists Indexes and splitting")
print('***************************')

list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(f'List: {list_1}')
print(f'First index: list[0] {list_1[0]}\nSecond Index: list[1]: {list_1[1]} and so on...')

# slicing the element
print(f'Slicing element to show index from 0 to 6')
print(list_1[0:6])

# by default the index values is 0 and so its start from the 0th element and go for index -1
print("The start denotes the starting index position of the list.\n"
      "The stop denotes the last index position of the list.\n"
      "The step is used to skip the nth element within a start:stop\n")

print(f'printing complete list                     => list[:]    : {list_1[:]}')
print(f'printing list from index 2 to 5            => list[2:5]  : {list_1[2:5]}')
print(f'printing list from index 1 to 6 skipping 2 => list[1:6:2]: {list_1[1:6:2]}')

print("Forward Direction => 0  1  2  3  4  5  6  7\n"
      "                    -8 -7 -6 -5 -4 -3 -2 -1 <= Backword Direction\n")
print(f'List: {list_1}')
print(f'list[-1]   : {list_1[-1]}')
print(f'list[-3:]  : {list_1[-3:]}')
print(f'list[:-1]  : {list_1[:-1]}')
print(f'list[-3:-1]: {list_1[-3:-1]}')

print('\n# updating list values')
print(list_1)
# It will assign value to the value to the second index
list_1[2] = 10
print(list_1)
# Adding multiple-element
list_1[1:3] = [89, 78]
print(list_1)
# It will add value at the end of the list
list_1[-1] = 25
print(list_1)

print('Removing element from list')
list_2 = [1, 2, 3, 4, 5, 6]
print(f'List: {list_2}')

print(f'It will assign value to the second index: list[2] = 10')
list_2[2] = 10
print(f'Updated list: {list_2}')

print('Adding multiple elements list[1:3] = [89, 78]')
list_2[1: 3] = [89, 78]
print(f'Updated list: {list_2}')

print('It will add value at the end of the list: list[-1] = 25')
list_2[-1] = 25
print(f'Updated list: {list_2}')

print('# repetition of list')
# declaring the list
list1 = [12, 14, 16, 18, 20]
print(f'List: {list1}')
# repetition operator *
l = list1 * 2
print(l)

# concatenation of two lists
# declaring the lists
list1 = [12, 14, 16, 18, 20]
list2 = [9, 10, 32, 54, 86]
# concatenation operator +
new_list = list1 + list2
print(new_list)
print(f'Size of list {list1} = {len(list1)}')

print('Iteration of the list')
for i in list1:
    print(i, end=" ")

print('\nmembership in list: return True or False')
print(f'12 in {list1} = {12 in list1}')
print(f'13 in {list1} = {13 in list1}')
print(f'14 in {list1} = {14 in list1}')

print('\niterating string list\n')
string_list = ["John", "David", "James", "Jonathan"]
for i in string_list:
    # The i variable will iterate over the elements of the List and contains each element in each iteration.
    print(i)
# Declaring the empty list
empty_list = []
# Number of elements will be entered by the user
n = int(input("Enter the number of elements in the list:"))
# for loop to take the input
for i in range(0, n):
    # The input is taken from the user and added to the list as the item
    empty_list.append(input("Enter the item:"))
print("printing the list items..")
# traversal loop to print the list items
for i in l:
    print(i, end="  ")

list_to_remove = [0, 1, 2, 3, 4]
print("printing original list: ")
for i in list:
    print(i, end=" ")
list_to_remove.remove(2)
print("\nprinting the list after the removal of first element...")
for i in list_to_remove:
    print(i, end=" ")
