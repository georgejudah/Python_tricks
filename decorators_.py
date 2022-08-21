# The Power of Decorators
# 1. Python Decorator Basics

# Now, what are decorators really? They “decorate” or “wrap” another
# function and let you execute code before and after the wrapped function runs.
# Decorators allow you to define reusable building blocks that can
# change or extend the behavior of other functions. And, they let you
# do that without permanently modifying the wrapped function itself.
# The function’s behavior changes only when it’s decorated.
# What might the implementation of a simple decorator look like? In
# basic terms, a decorator is a callable that takes a callable as input and
# returns another callable.

def null_decorator(func):
    return func

# As you can see, null_decorator is a callable (it’s a function), it takes
# another callable as its input, and it returns the same input callable
# without modifying it

# Let’s use it to decorate (or wrap) another function:
def greet():
    return 'Hello!'

greet = null_decorator(greet)
print(greet())

# Instead of explicitly calling null_decorator on greet and then reassigning the greet variable, you can use Python’s @ syntax for decorating a function more conveniently:

@null_decorator
def greet():
    return 'Hi'

print(greet())

# Putting an @null_decorator line in front of the function definition is
# the same as defining the function first and then running through the
# decorator. Using the @ syntax is just syntactic sugar and a shortcut
# for this commonly used pattern.



# 2. Decorators Can Modify Behavior
# Now that you’re a little more familiar with the decorator syntax, let’s
# write another decorator that actually does something and modifies the
# behavior of the decorated function.

# Here’s a slightly more complex decorator which converts the result of
# the decorated function to uppercase letters:

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

# Note how, up until now, the decorated function has never been executed. Actually calling the input function at this point wouldn’t make
# any sense—you’ll want the decorator to be able to modify the behavior
# of its input function when it eventually gets called.
@uppercase
def greet():
    return "Hi I have been decorated"
print(greet())

# And as you saw earlier, it needs to do that in order to modify the
# behavior of the decorated function when it finally gets called. The
# uppercase decorator is a function itself. And the only way to influence
# the “future behavior” of an input function it decorates is to replace (or
# wrap) the input function with a closure.
# That’s why uppercase defines and returns another function (the closure) that can then be called at a later time, run the original input
# function, and modify its result.
# Decorators modify the behavior of a callable through a wrapper closure so you don’t have to permanently modify the original. The original callable isn’t permanently modified—its behavior changes only
# when decorated.
# This let’s you tack on reusable building blocks, like logging and other
# instrumentation, to existing functions and classes. It makes decorators such a powerful feature in Python that it’s frequently used in the
# standard library and in third-party packages.
# in the above code - the nested function is able to call the func passed to the parent function - that's closure(check effective_functions.py file)

# https://pythontutor.com/render.html#mode=display - Use this website to paste the above greet function and the upper case decorator and see step by step


#3. Applying Multiple Decorators to a Function
def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

@strong
@emphasis
def greet():
    return("Hello")

print(greet())

# This clearly shows in what order the decorators were applied: from
# bottom to top. First, the input function was wrapped by the @emphasis
# decorator, and then the resulting (decorated) function got wrapped
# again by the @strong decorator.
# To help me remember this bottom to top order, I like to call this behavior decorator stacking. You start building the stack at the bottom
# and then keep adding new blocks on top to work your way upwards


# If you break down the above example and avoid the @ syntax to apply
# the decorators, the chain of decorator function calls looks like this:
decorated_greet = strong(emphasis(greet))


# Note:
# This also means that deep levels of decorator stacking will evenutally
# have an effect on performance because they keep adding nested
# function calls. In practice, this usually won’t be a problem, but
# it’s something to keep in mind if you’re working on performanceintensive code that frequently uses decoration.


# How to Write “Debuggable” Decorators
# def greet():
# """Return a friendly greeting."""
# return 'Hello!'
# decorated_greet = uppercase(greet)
#  you try to access any of that function metadata, you’ll see the wrapper closure’s metadata instead:

# >>> greet.__name__
# 'greet'
# >>> greet.__doc__
# 'Return a friendly greeting.'
# >>> decorated_greet.__name__
# 'wrapper'
# >>> decorated_greet.__doc__
# None

# This makes debugging and working with the Python interpreter
# awkward and challenging. Thankfully there’s a quick fix for this: the
# functools.wraps decorator included in Python’s standard library.4
# You can use functools.wraps in your own decorators to copy over the
# lost metadata from the undecorated function to the decorator closure.
# Here’s an example

# import functools
# def uppercase(func):
# @functools.wraps(func)
# def wrapper():
# return func().upper()
# return wrapper
# Applying functools.wraps to the wrapper closure returned by the
# decorator carries over the docstring and other metadata of the input
# function:
# @uppercase
# def greet():
# """Return a friendly greeting."""
# return 'Hello!'
# >>> greet.__name__
# 'greet'
# >>> greet.__doc__
# 'Return a friendly greeting.'
# As a best practice, I’d recommend that you use functools.wraps in
# all of the decorators you write yourself. It doesn’t take much time and
# it will save you (and others) debugging headaches down the road.

# Key Takeaways:
#  .Decorators define reusable building blocks you can apply to a
# callable to modify its behavior without permanently modifying
# the callable itself.
#  The @ syntax is just a shorthand for calling the decorator on
# an input function. Multiple decorators on a single function are
# applied bottom to top (decorator stacking).
# • As a debugging best practice, use the functools.wraps helper
# in your own decorators to carry over metadata from the undecorated callable to the decorated one.
# • Just like any other tool in the software development toolbox,
# decorators are not a cure-all and they should not be overused.
# It’s important to balance the need to “get stuff done” with the
# goal of “not getting tangled up in a horrible, unmaintainable
# mess of a code base.”



