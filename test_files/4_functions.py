def no_return_function():
    num1 = 10
    num2 = 20
    addition = num1 + num2


number = no_return_function()
print(number)


def with_return_function(num):
    x = ''
    if num % 2 == 0:
        x = 'Even Number'
    else:
        x = 'Odd Number'
    return x


result = with_return_function(10)
print(result)
