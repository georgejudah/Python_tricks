squares = [x*x for x in range(10)]
# template - values = [expression for item in collection]

# The key to understanding list comprehensions is that they’re just for-
# loops over a collection but expressed in a more terse and compact syn-
# tax.
# This is sometimes referred to as syntactic sugar—a little shortcut for
# frequently used functionality that makes our lives as Python coders
# easier.

#using conditions inside list comprehension
even_squares = [x * x for x in range(10) if x % 2 == 0]
print(squares)
print(even_squares)

# Key Takeaways
# • Comprehensions are a key feature in Python. Understanding
# and applying them will make your code much more Pythonic.

# • Comprehensions are just fancy syntactic sugar for a simple for-
# loop pattern. Once you understand the pattern, you’ll develop

# an intuitive understanding for comprehensions.
# • There are more than just list comprehensions.