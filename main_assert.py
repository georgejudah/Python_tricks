#Assertion in python
# You’ll learn how to use them to help automatically

# detect errors in your Python programs. This will make your programs
# more reliable and easier to debug.
# At this point, you might be wondering “What are assertions and what
# are they good for?” Let’s get you some answers for that.
# At its core, Python’s assert statement is a debugging aid that tests a
# condition. If the assert condition is true, nothing happens, and your

# program continues to execute as normal. But if the condition evalu-
# ates to false, an AssertionError exception is raised with an optional

# error message.

def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price

#It will guarantee that, no matter what, discounted prices calculated by this function cannot be lower
#than $0 and they cannot be higher than the original price of the prod-uct.

shoes = {'name': 'Fancy Shoes', 'price': 14900}
# apply_discount(shoes, 0.25)

#let’s try to apply some invalid discounts.
apply_discount(shoes, 2.0)

#This speeds up debugging efforts considerably, and it will make your
# programs more maintainable in the long-run. And that, my friend, is
# the power of assertions.

# You see, the proper use of assertions is to inform developers about
# unrecoverable errors in a program. Assertions are not intended to
# signal expected error conditions, like a File-Not-Found error, where
# a user can take corrective actions or just try again.

#GOTO literal_string_interpolation