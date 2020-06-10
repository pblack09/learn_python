            # 8: Printing, Printing
formatter = "{} {} {} {}"
    # Above it the variable for "formula"
    # Below we insert values into the brackets by adding ".format" after the variable name
    # Each item added in is called an "Argument"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "You can also",
    "break up the entries",
    "into multiple lines",
    "followed by a comma."
))
print(formatter.format("What if", "I only", "Use 3 arguments?", "(It won't work)"))