# So what are *args and **kwargs parameters used for? They allow a
# function to accept optional arguments, so you can create flexible APIs
# in your modules and classes:

def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(f'args here {args}')
    if kwargs:
        print(f'kwargs here {kwargs}')
        # you can also access individual kwarg using the below syntax
        # print(kwargs['key1'])

foo('hello')
foo('world', 1 ,2, 3)
foo('hello world', 3, 4, 5, key1 = 'Hi', key2 = 'There')

# I want to make it clear that calling the parameters args and kwargs is
# simply a naming convention. The previous example would work just
# as well if you called them *parms and **argv. The actual syntax is
# just the asterisk (*) or double asterisk (**), respectively

# However, I recommend that you stick with the accepted naming convention to avoid confusion

# You can also forward optional arguments or keyboard arguments to other functinos
