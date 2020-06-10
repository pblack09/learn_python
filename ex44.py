            # 44: Inheritance vs Composition


            #INHERITANCE

class Parent(object):
    # Here, the implicit function only exists in the
    # Parent class, so the Child class inherits the
    # same output.
    def implicit(self):
        print("PARENT implicit()")

    # Both Parent and Child classes have the override
    # function, so Child class will use its' instance
    # if called.
    def override(self):
        print("PARENT override()")

    # The Child class 'altered' function has a different
    # set of outputs from the Parent class' function,
    # which doesn't inherit from the Child class
    def altered(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        print("CHILD, override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
            # Super() calls the Parent class function with the
            # given arguments
            # ex) super(Child, self).altered()
            # calls the super of Child() = Parent()
            # calls the altered() function with arg 'self'
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()


            # COMPOSITION

    # Here the 2 classes are NOT related. Both are separate,
    # but they can use each other's functions or attributes
    # if called like normally

class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Different(object):

        # This sets 'self.other' equal to calling from
        # class Other() like usual
    def __init__(self):
        self.other = Other()

        # Here implicit() is basically saying:
        # class1 = Other()
        # class1.implicit()
    def implicit(self):
        self.other.implicit()

    def override(self):
        print("DIFFERENT override()")

    def altered(self):
        print("DIFFERENT BEFORE altered()")
        self.other.altered()
        print("DIFFERENT AFTER altered()")

class2 = Different()

class2.implicit()
class2.override()
class2.altered()
