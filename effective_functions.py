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


