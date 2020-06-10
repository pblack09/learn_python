            # 15: Reading Files
    # Find the file
from sys import argv
    # The 1st argument dictates which script is executed
    # The 2nd argument dictates which file to open given the following functions
script, filename = argv
    # Assign a variable to open given file name
txt = open(filename)
    # Use the variable to open the file
print(f"Here's your file {filename}:")
print(txt.read())
    # Starting here without giving a filename yet prompts the User for the filename now:
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

    # .text() tells the file to print out what it contains
    
    # If you delete lines 6-11 and only have "script = argv",
    # then you don't have to provide the filename in the initial
    # command line. The script will prompt the User for the
    # filename after the script has been opened.
    
    # "txt = open(file)" only shows what's in the file. It does not
    # place any values into functions, integers, etc.
    
    # You can "read" any type of file. You could even use this:
    # $ python ex15.py ex15.py
    # The above will use this script to show the text of this script.