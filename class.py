      # 40: Modules, Classes, and Objects

# Imagine we have a module named mystuff.py with a dict {'apples': 'I AM APPLES!'},
# a function named apple(): print("I AM APPLES!"), and a variable of
# tangerine = "Living reflection of a dream".

# We can import the module and use the dict, function, or variable using a "." modifier;
# import mystuff

# mystuff.apple()
# mystuff.['apples']
# mystuff.tangerine

# Here we can create a class just like the mystuff module:
class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

#               **instantiate: fancy word for "create"**

# We can set the class or mini-module to a variable and call it's functions, variables, etc.
# just like when we import mystuff.py
thing = MyStuff()       # This is the 'instantiate' operation
thing.apple()           # Prints 'I AM CLASSY APPLES'
print(thing.tangerine)  # Prints 'And now a thousand years between'
print(thing.__init__()) # Prints 'None'

# Classes are like definitions for creating new mini-modules
# Instantiation is how you make one of these mini-modules and import it at the same time
# The resulting mini-module is called an 'object' and you then assign it to a variable
