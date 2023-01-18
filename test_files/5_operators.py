# is keyword is the substitute of ==
print(True is True)
print(True is False)
print(None is not None)

# A blank dictionary or list is the same as another blank one. However, they aren't identical entities because they
# are stored independently in memory. This is because both the list and the dictionary are changeable.
print([] == [])
print([] is [])
print({} == {})
print({} is {})

# nolocal
'''Nonlocal keyword usage is fairly analogous to global keyword usage. The keyword nonlocal is designed to indicate 
that a variable within a function that is inside a function, i.e., a nested function is just not local to it, 
implying that it is located in the outer function. We must define a non-local parameter with nonlocal if we ever need 
to change its value under a nested function. Otherwise, the nested function creates a local variable using that 
title. The example below will assist us in clarifying this.'''


def the_outer_function():
    var = 10

    def the_inner_function():
        nonlocal var
        var = 14
        print("The value inside the inner function: ", var)

    the_inner_function()
    print("The value inside the outer function: ", var)


the_outer_function()


def the_outer_function_without_nolocal():
    var_1 = 10

    def the_inner_function():
        var_1 = 14
        print("Value inside the inner function: ", var_1)

    the_inner_function()
    print("Value inside the outer function: ", var_1)


the_outer_function()
