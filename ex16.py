            # 16: Reading and Writing Files
    # Find given filename
from sys import argv
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
    # Enables User to back out based on their next input.
input("?")

print("Opening the file...")
target = open(filename, 'w')
print("Truncating the file. Goodbye!")
target.truncate()
    # filename.truncate() just deleted all of the text in the file, but not the file itself.
print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

target.write(f"{line1}\n{line2}\n{line3}")
    # filename.write() adds text into the desired file.
print("And finally, we close it.")
target.close()
    # filename.close() finally closes the file from any further modifications.
    # At least until pulled up again.