for i in range(15):
    print(i + 4, end=" ")
    # breaking the loop when i = 9
    if i == 9:
        break
print()


# looping from 1 to 15
i = 0  # initial condition
while i < 15:

    # When i has value 9, loop will jump to next iteration using continue. It will not print
    if i == 9:
        i += 3
        continue
    else:
        # when i is not equal to 9, adding 2 and printing the value
        print(i + 2, end=" ")

    i += 1