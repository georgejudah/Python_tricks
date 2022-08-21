# Python’s Functions Are First-Class

# just like how strings, lists, modules, are all objects in python, likewise functions are first class objects as well

def yell(text):
    print(text.upper() + '!')
    return text.upper() + '!'

yell('hello')

# Because the yell function is an object in Python, you can assign it to
# another variable, just like any other object:

bark = yell
bark('Wow')

# Function objects and their names are two separate concerns. Here’s
# more proof: You can delete the function’s original name (yell). Since
# another name (bark) still points to the underlying function, you can
# still call the function through it:
#uncomment below 2 lines of code and try it
# del yell

# yell('hello?')

# now, comment the above 2 lines of code and uncomment the below line 
# bark('This is awesome')

# By the way, Python attaches a string identifier to every function at
# creation time for debugging purposes. You can access this internal
# identifier with the __name__ attribute:

# print(bark.__name__)

# Now, while the function’s __name__ is still “yell,” that doesn’t affect
# how you can access the function object from your code. The name
# identifier is merely a debugging aid. A variable pointing to a function
# and the function itself are really two separate concerns.

# Functions Can Be Stored in Data Structures

# Since functions are first-class citizens, you can store them in data
# structures, just like you can with other objects. For example, you can
# add functions to a list:
#uncomment these 4 lines of code and try
# funcs = [bark, str.lower, str.capitalize]
# print(funcs)

# for f in funcs:
#     print(f('Hey there'))

# funcs[0]('heyho')

# Functions Can Be Passed to Other Functions
def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)

greet(bark)

# Functions Can be Nested
def speak(text):
    def whisper(t):
        return t.lower() + '....'
    return whisper(text)

speak("Hi there")
#it is good to note that, the inner function whisper() does not exist
# outside speak ()



# Functions can be defined inside other functions—and a
# child function can capture the parent function’s local state (lexical closures)
# Functions Can Capture Local State
def get_speak_func(text, volume):
    def whisper():
        return text.lower() + '...'
    def yell():
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper
# Take a good look at the inner functions whisper and yell now. Notice
# how they no longer have a text parameter? But somehow they can
# still access the text parameter defined in the parent function. In fact,
# they seem to capture and “remember” the value of that argument.
# Functions that do this are called lexical closures (or just closures, for
# short). A closure remembers the values from its enclosing lexical
# scope even when the program flow is no longer in that scope.

# In practical terms, this means not only can functions return behaviors
# but they can also pre-configure those behaviors. Here’s another barebones example to illustrate this idea:
def make_adder(n):
    def add(x):
        return x + n
    return add

plus_5 = make_adder(5)
print(plus_5(4))




# Objects Can Behave Like Functions
# While all functions are objects in Python, the reverse isn’t true. Objects aren’t functions. But they can be made callable, which allows
# you to treat them like functions in many cases.
# If an object is callable it means you can use the round parentheses
# function call syntax on it and even pass in function call arguments.
# This is all powered by the __call__ dunder method. Here’s an example of class defining a callable object

class Adder:
    def __init__(self, n):
        self.n = n
        print(n)
    def __call__(self, x):
        return self.n + x

plus_3 = Adder(3)
a = plus_3(4)
print(a)
# Behind the scenes, “calling” an object instance as a function attempts
# to execute the object’s __call__ method.

# Of course, not all objects will be callable. That’s why there’s a built-in
# callable function to check whether an object appears to be callable
# or not:
print(callable(plus_3))

# Key Takeaways
# • Everything in Python is an object, including functions. You can
# assign them to variables, store them in data structures, and pass
# or return them to and from other functions (first-class functions.)
# • First-class functions allow you to abstract away and pass
# around behavior in your programs.
# • Functions can be nested and they can capture and carry some
# of the parent function’s state with them. Functions that do this
# are called closures.
# • Objects can be made callable. In many cases this allows you to
# treat them like functions


# Lambda Functions
# lambda keyword in python provides a shortcut for declaring small anonymous functions
# Lambda functions behave just like
# regular functions declared with the def keyword. They can be used
# whenever function objects are required.

add = lambda x,y: x + y
print(add(5,3))

# You could declare the same add function with the def keyword, but it
# would be slightly more verbose:
def add(x,y):
    return x + y
print(add(5,3))

print((lambda x,y: x + y)(5, 3))
# Conceptually, the lambda expression lambda x, y: x + y is the
# same as declaring a function with def, but just written inline. The
# key difference here is that I didn’t have to bind the function object to
# a name before I used it. I simply stated the expression I wanted to
# compute as part of a lambda, and then immediately evaluated it by
# calling the lambda expression like a regular function.

# There’s another syntactic difference between lambdas and regular
# function definitions. Lambda functions are restricted to a single
# expression. This means a lambda function can’t use statements or
# annotations—not even a return statement.
# How do you return values from lambdas then? Executing a lambda
# function evaluates its expression and then automatically returns
# the expression’s result, so there’s always an implicit return statement. That’s why some people refer to lambdas as single expression
# functions.

# But Maybe You Shouldn’t…
# On the one hand, I’m hoping this chapter got you interested in exploring Python’s lambda functions. On the other hand, I feel like it’s time
# to put up another caveat: Lambda functions should be used sparingly
# and with extraordinary care.
# I know I’ve written my fair share of code using lambdas that looked
# “cool” but were actually a liability for me and my coworkers. If you’re
# tempted to use a lambda, spend a few seconds (or minutes) to think
# if it is really the cleanest and most maintainable way to achieve the
# desired result.
# For example, doing something like this to save two lines of code is just
# silly. Sure, technically it works and it’s a nice enough “trick.” But it’s
# also going to confuse the next gal or guy that has to ship a bugfix under
# a tight deadline:

# If you find yourself doing anything remotely complex with lambda
# expressions, consider defining a standalone function with a proper
# name instead.


# Key Takeaways
# • Lambda functions are single-expression functions that are not
# necessarily bound to a name (anonymous).
# • Lambda functions can’t use regular Python statements and always include an implicit return statement.
# • Always ask yourself: Would using a regular (named) function
# or a list comprehension offer more clarity?



