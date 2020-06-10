      # 41: Learning to Speak Object-Oriented

word_drills = {
    "class": "Tell Python to make a new type of thing",
    "object": "1) Most basic type of thing, 2) Any instance of some thing",
    "instance": "What you get when you tell Python to make a class",
    "def": "How you define a function inside a class",
    "self": "Inside the functions in a class, self is a variable for the instance/object being accessed",
    "inheritence": "Concept that a class can inherit traits from a parent class",
    "composition": "Concept that a class can be composed of other classes",
    "attribute": "A property classes have that are from composition and are usually variables",
    "is-a": "A phrase to say that something inherits from another ex.) salmon is-a fish",
    "has-a": "A phrase to say that something is composed of other things ex.) salmon has-a mouth"
}

phrase_drills = {
    "class X(Y)": "Make a class named X that is-a Y",
    "class X(object): def __init__(self, J)": "Class X has-a __init__ that takes self and J parameters",
    "class X(object): def M(self, J)": "Class X has-a function named M that takes self and J parameters",
    "foo = X()": "Set foo to an instance of class X",
    "foo.M(J)": "From foo, get the M function, and call it with parameters self, J",
    "foo.K = Q": "From foo, get the K attritbute, and set it to Q"
}
