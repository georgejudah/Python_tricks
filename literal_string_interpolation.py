# #Python 3.6 adds yet another way to format strings, called Formatted

# String Literals. This new way of formatting strings lets you use em-
# bedded Python expressions inside string constants. Here’s a simple

# example to give you a feel for the feature:

#well, I already knew we could use variables inside string constants, but it's essentially not just variables but rather Python expressions

a = 6
b = 5

print(f"Six plus 5 equals {6+5} and not {2* (a+b)}")


# BEHIND THE SCENES
def greet(name, question):
    return f"Hello, {name}! How's it {question}?"

# greet('Bob', 'going')

# When we disassemble the function and inspect what’s going on be-
# hind the scenes, we can see that the f-string in the function gets trans-
# formed into something similar to the following:

def greet(name, question):
    return ("Hello, " + name + "! How's it " +

question + "?")


#Template Strings
# One more technique for string formatting in Python is Template
# Strings. It’s a simpler and less powerful mechanism, but in some
# cases this might be exactly what you’re looking for.

name = "bob"
from string import Template
t = Template('Hey, $name!')
t.substitute(name=name)

# Another difference is that template strings don’t allow format speci-
# fiers. So in order to get our error string example to work, we need to

#when to use template strings
# In my opinion, the best use

# case for template strings is when you’re handling format strings gen-
# erated by users of your program. Due to their reduced complexity,

# template strings are a safer choice.

# transform our int error number into a hex-string ourselves:
# I’m using the %s format specifier here to tell Python where to substi-
# tute the value of name, represented as a string. This is called “old style”
# string formatting.
# example
# 'Hello, %s' % name 

#String formatting Thumb rule - by Dan
# If your format strings are user-supplied, use Template
# Strings to avoid security issues. Otherwise, use Literal
# String Interpolation if you’re on Python 3.6+, and “New
# Style” String Formatting if you’re not.

#GOTO Zen of python.py