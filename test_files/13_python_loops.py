# Python program to show how the for loop works

# Creating a sequence which is a tuple of numbers
numbers = [4, 2, 6, 7, 3, 5, 8, 10, 6, 1, 9, 2]

# variable to store the square of the number
square = 0

# Creating an empty list
squares = []

# Creating a for loop
for value in numbers:
    square = value ** 2
    squares.append(square)
print("The list of squares is", squares)

# Python program to show how if-else statements work

string = "Python Loop"

# Initiating a loop
for s in string:
    # giving a condition in if block
    if s == "o":
        print("If block")
        # if condition is not satisfied then else block will be executed
    else:
        print(s)

# Python program to show how to use else statement with for loop

# Creating a sequence
tuple_ = (3, 4, 6, 8, 9, 2, 3, 8, 9, 7)

# Initiating the loop
for value in tuple_:
    if value % 2 != 0:
        print(value)
    # giving an else statement
else:
    print("These are the odd numbers present in the tuple")

# Python program to show the working of range() function

print(range(15))

print(list(range(15)))

print(list(range(4, 9)))

print(list(range(5, 25, 4)))

# Python program to iterate over a sequence with the help of indexing

tuple_ = ("Python", "Loops", "Sequence", "Condition", "Range")

# iterating over tuple_ using range() function
for iterator in range(len(tuple_)):
    print(tuple_[iterator].upper())

# Python program to show how to use a while loop
counter = 0
# Initiating the loop
while counter < 10:  # giving the condition
    counter = counter + 3
    print("Python Loops")

# Python program to show how to use else statement with the while loop
counter = 0

# Iterating through the while loop
while counter < 10:
    counter = counter + 3
    print("Python Loops")  # Executed until condition is met
# Once the condition of while loop gives False this statement will be executed
else:
    print("Code block inside the else statement")

# Python program to show how the continue statement works

# Initiating the loop
for string in "Python Loops":
    if string == "o" or string == "p" or string == "t":
        continue
    print('Current Letter:', string)

# Python program to show how the break statement works

# Initiating the loop
for string in "Python Loops":
    if string == 'L':
        break
    print('Current Letter: ', string)

# Python program to show how the pass statement works
for string in "Python Loops":
    pass
print('Last Letter: ', string)

# range function
my_list = [3, 5, 7, 9]
print(f'Original List: {my_list}')
for iter_var in range(len(my_list)):
    my_list.append(my_list[iter_var] + 2)

print(f'List after executing the for loop: {my_list}')

# creating the list of numbers
number = [3, 5, 23, 6, 5, 1, 2, 9, 8]

# initilizing a variable that will store the sum
sum_ = 0

# using for loop to iterate over the list
for num in number:
    sum_ = sum_ + num ** 2

print(f'Number list: {number}')
print(f'The sum of square is: {sum_}')

# iterating by using index of sequence

# using else statement in for loop
# code to print marks of a student from the record
student_name_1 = 'Itika'
student_name_2 = 'Parker'

# creating a dictionary of students records
records = {'Itika': 90, 'Arshia': 92, 'Peter': 98}


def get_record(student_name):
    for a_student in records:  # for loop will iterate over the keys of the dictionary
        if a_student == student_name:
            return records[a_student]
            break
        else:
            return f'There is no record found for {student_name} in the records'


print(f'Marks of {student_name_1} are: {get_record(student_name_1)}')
print(f'Marks of {student_name_2} are: {get_record(student_name_2)}')
