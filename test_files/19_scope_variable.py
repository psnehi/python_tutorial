def number():
    num = 50
    print(f'Value of num inside function: {num}')


num = 10
number()
print(f'Value of variable num: {num}')


# nested function
def word():
    string = 'Python nested function'
    x = 5

    def number_function():
        print(string)
        print(x)

    number_function()


word()
