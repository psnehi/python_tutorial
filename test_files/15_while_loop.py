num = 10

# initializing summation and a counter for iteration
summation = 0
sum_ = 0
c = 1
list_ = []

while c <= num:  # specifying the condition of the loop
    """Beginning the code block"""
    list_.append(c)
    sum_ += c
    summation = c ** 2 + summation
    c = c + 1  # incrementing the counter

# printing final sum
print(f'Teh sum of of the list {list_} is: {sum_}')
print(f'Teh sum of squares of the list {list_} is: {summation}')

# prime number
num = [34, 12, 54, 23, 75, 34, 11]


def prime_number(number):
    condition = 0
    iteration = 2
    while iteration <= number / 2:
        if number % iteration == 0:
            condition = 1
            break

        iteration += 1

    if condition == 0:
        print(f'{number} is a PRIME number')
    else:
        print(f'{number} is not a PRIME number')


# checking prime numbers from list using for loop
for i in num:
    prime_number(i)

# multiplication
num = int(input("Please enter any number to print table: "))
counter = 1
# we will use a while loop for iterating 10 times for the multiplication table
print("The Multiplication Table of: ", num)
while counter <= 10:  # specifying the condition
    ans = num * counter
    print(f'{num} x {counter} = {ans}', end="     ")
    counter += 1  # expression to increment the counter

print(end="\n")


# Python program to square every number of a list
# initializing a list
list_ = [3, 5, 1, 4, 6]
print(f'Original list: {list_}')
squares = []
# programing a while loop
while list_:  # until list is not empty this expression will give boolean True after that False
    squares.append((list_.pop()) ** 2)
# print the squares
print(f'Print square of the list: {list_}: {squares}')


