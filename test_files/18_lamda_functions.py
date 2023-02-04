from typing import Callable, Any

print('''The Anonymous Functions
These types of Python functions are anonymous since we do not declare them, as we declare usual functions, using the 
def keyword. We can use the lambda keyword to define the short, single output, anonymous functions.
Lambda expressions can accept an unlimited number of arguments; however, they only return one value as the result of the 
function. They can't have numerous expressions or instructions in them. Since lambda needs an expression, an anonymous 
function cannot be directly called to print.

Lambda functions contain their unique local domain, meaning they can only reference variables in their argument list and 
the global domain name.

Although lambda expressions seem to be a one-line representation of a function, they are not like inline expressions in 
C and C++, which pass function stack allocations at execution for efficiency concerns.''')

print('Syntax\n'
      '\n'
      'Lambda functions have exactly one line in their syntax:\n'
      '\n'
      'lambda [argument1 [,argument2... .argument]] : expression    \n')

_lambda: Callable[[Any, Any, Any], Any] = lambda arg1, arg2, arg3: arg1 + arg2 + arg3
print(f'_lambda(1, 2, 3): {_lambda(1, 2, 3)}')

_lambda_1: Callable[[Any, Any], Any] = lambda argument1, argument2: argument1 + argument2

# calling function
print(f'Value of the function is: {_lambda_1(20, 30)}')
print(f'Value of the function is: {_lambda_1(40, 50)}')
