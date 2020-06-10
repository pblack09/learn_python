            # 13: Parameters, Unpacking, Variables
    # "sys" is the module being pulled from
    # "modules" are aka "libraries" since they hold information
    # "argv" is the "argument variable" which holds other variables
from sys import argv
    # This unpacks argv into 4 different variables
script, first, second, third = argv

print("The script is called:", script)
print("Your first number is:", first)
print("Your second number is:", second)
print("Your third string is:", third)
    # You can add int() to make the arguments integers
print(int(first) + int(second))
    # Here is how to call it in command line:
#$ python learn2.py stuff things that
#The script is called: learn2.py
#Your first variable is: stuff
#Your second variable is: things
#Your third variable is: that

    # Less than the required arguments will push back a ValueError

    # Here we can combine an argument with a user input in 1 command
    # We can't use an input as an argument ex.) input() = argv
print("What is your favorite color?", end=' ')
color = input()
print(f"Your favorite color is {color} and my favorite number is ", second)