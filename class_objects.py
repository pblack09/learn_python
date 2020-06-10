      # 42: Is-A, Has-A, Objects, and Classes

#is-a
class Animal(object):
    pass

#is-a
class Dog(Animal):

    def __init__(self, name):
        #has-a
        self.name = name

#is-a
class Cat(Animal):

    def __init__(self, name):
        #has-a
        self.name = name

#is-a
class Person(object):

    def __init__(self, name):
        #has-a
        self.name = name
        #has-a
        self.pet = None

#is-a
class Employee(Person):

    def __init__(self, name, salary):
        #has-a
        super(Employee, self).__init__(name)
        #has-a
        self.salary = salary

#is-a
class Fish(object):
    pass

#is-a
class Salmon(Fish):
    pass

#is-a
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")
#is-a
satan = Cat("Satan")
#is-a
mary = Person("Mary")
# Mary has-a pet named satan
mary.pet = satan
#has-a
frank = Employee("Frank", 120000)
#has-a
frank.pet = rover
# flipper is-a part of Fish
flipper = Fish()
#is-a
crouse = Salmon()
#is-a
harry = Halibut()
