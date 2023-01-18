'''
    The pass Keyword
In Python, a null sentence is called a pass. It serves as a stand-in for something else. When it is run, nothing occurs.
Let's say we possess a function that has not been coded yet however we wish to do so in the long term. If we write just
this in the middle of code,
'''


def function_pass(argument):
    pass


# we can use pass keyword to create an empty class too
class passed_class:
    pass


# return keyword
def func_with_return():
    var = 13
    return var


def fun_without_return():
    var = 10


print(func_with_return())

print(fun_without_return())

# del keyword to remove any reference to object
'''
    var_1 = var_2 = 5
    del var_1
    print(var_2)
    print(var_1)
'''

list_ = ['A', 'B', 'C']
print(list_)
del list_[2]
print(list_)

