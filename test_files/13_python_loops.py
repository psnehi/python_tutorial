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
while counter < 10: # giving the condition
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
