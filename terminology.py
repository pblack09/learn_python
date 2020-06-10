            # 22: What Do You Know So Far?

#
    Lets you add comments in the code that are not executed by the script
~
    The home network for the terminal (usually under C:/Users/phili
+ - / *
    Add, subtract, divide, multiply
%
    (Modulo) Divides the given values and gives you the remainder, ex) 9 % 2 = 5
< > <= >=
    Less than, greater than, less than or equal, greater than or equal
+=
    Adds to the current value of a variable
' : '
    When at the end of a line, states that the following line applies to what comes before the colon
\
    Encodes difficult-to-type characters into a string
\\
    Adds a single \ into a string if needed
\a
    ASCII bell (BEL)
\b
    ASCII backspace (BS)
\f
    ASCII formfeed (FF)
\n
    Skips to the next line; ASCII linefeed (LF)
\N{name}
    Character named name in the Unicode database {Unicode only}
\r
    Carriage Return (CR)
\t
    Tabs over 1 place
\uxxxx
    Character with 16-bit hex value
\Uxxxxxxxx
    Character with 32-bit hex value
\v
    ASCII vertical tab (VT)
\000
    Character with octal value 000
\xhh
    Character with hex value hh
"""
    3 quotations make everything a string regardless of which line it is on
    until the next 3 quotations marks
    """
==
    A boolean factor that checks if 2 things are equal
!=
    A boolean factor that checks if 2 things are NOT equal
'a' or 'a+'
    File is in 'append' mode; Adds to file contents; Starts at end of file
'r' or 'r+'
    File is in 'read-only' mode; Only shows the file contents; Starts at top of file
'w' or 'w+'
    File is in 'write' mode; Erases current contents of file for new contents; Starts at top of file
.close()
    Closes a file after being opened and used within a script
.format()
    Assigns an argument to the function it is attached to
.read()
    A command that reads the file it is attached to
.readline()
    Reads the given number of lines from the file
.seek()
    Seeks a certain point in a file to start from; Usually used as ".seek(0)" to move to the start of the file
.truncate()
    Erases contents of the file
.write()
    Adds to the file
Argument
    A condition given to a function; Usually a variable, string, or number
argv
    "Argument Variable" is a variable that holds the argument(s) given to the script
Boolean
    Something that states if something is True or False; this is fact-based
call
    Starts something; aka "run" or "use"
command line
    A terminal on your computer that you can open/edit/create from
Concatenate
    Link a series together
DataType
    How a character is defined; ex.) String: "Hello", Integer: 2, Floating Point: 2.3
def
    Defines a function; ex.) def test_function will define what "test_function" does
Escape Sequence
    Lets you use characters that are not normally allowed in strings
Floating Point
    Number with a decimal point ex.) 4.0
Format String
    A string that can use variables ex.) print(f"Here is my text. Here is the {variable}.")
Function
    A command that performs an assigned task; can be modified by multiple different means
import
    Adding something to your python script from outside
input()
    Requests and takes input from the User; can be any data type and assigned to any variable by using "int(input())", "float(input())", etc.
Integer
    Whole number ex.) 4
len()
    Shows the length of a string and translates it to a number
modules
    aka 'libraries', hold a lot of information, commands, etc. that are stored away until imported into the code
NameError
    When something is used that does not exist (Mostly with unassigned variables)
octothorpe
    '#'
Parameter
    Conditions that apply to a command or function
print()
    Prints text into the command line
prompt
    What is given by the User for an input; ex.) input(prompt)
quit()
    Quits the script; Not typically used in the code, unless to make the interaction more user-friendly
run
    Starts something; aka "call" or "use"
"Sample text."   'Also sample text.'   "You can even 'combine' the 2."   'My mom said "Hello" to you.'
    This is a string which is a series of characters
Script
    A series of commands
SyntaxError
    There is an error in the code writing
sys
    The system module; Usually connects to the command line when running a script for input or to pull other information from
use
    Starts something; aka "call" or "run"
Variable
    A given name that has an assigned value, string, or function; can NOT start with a number, but can use letters, numbers, or _
ValueError
    When there are not enough given values to perform a function; ellipsisx.) function(1, 2, 3)   User only gives (1, 2)