# Here's an example of inheritance or having a parent/child class
# aka Superclass
class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*self.length + 2*self.width

rectangle = Rectangle(2, 4)
rectangle.area()

class Square(Rectangle):
    def __init__(self, length, **kwargs):
        # Here super() calls the original __init__ from class Rectangle
        super().__init__(length=length, width=length, **kwargs)
        # super().__init__ and super(Square, self).__init__
        # both do the same things (Look below for where this is useful)
        # because it's calling the super() of Square
        # super().------- will be used almost all times

square = Square(4)
square.area()

# Another layer added on
class Cube(Square):
    # Doesn't need an __init__ because it inherits that from class Square
    def surface_area(self):
        # Here we take the original area() function and set it to face_area
        face_area = super().area()
        # If we wanted to avoid using the Square() .area() function, we can use
        # super(Square, self).area()
        # This will look to the super() of Square() which takes us to Rectangle()
        # This is useful IF square.area() was not the correct .area() function
        # that we want to use for Cube()
        return face_area*6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

cube = Cube(3)
cube.surface_area()
cube.volume()

# Here's another layer introducing sibling classes, or a class that inherits
# from more than 1 parent class

class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)

    def tri_area(self):
        return .5 * self.base * self.height


class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(base=base, **kwargs)
        # This uses super() to call class Square's __init__ with
        # 'self.base' in place of Square's 'length' parameter

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return .5 * perimeter * self.slant_height * base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area

pyramid = RightPyramid(2, 4)
print(pyramid.area())
print(pyramid.area_2())
RightPyramid.__mro__
    # The .__mro__ attribute can be called to any class to see the order
    # of which classes it will search through
    # Order: Own class > 1st class in params > any supers to 1st class >
    # > 2nd class in params > any supers to 2nd class
