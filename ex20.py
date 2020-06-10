            # 20: Functions and Files

from sys import argv
script, input_file = argv

    # Define our functions
def print_all(f):
    print(f.read())
def rewind(f):
    f.seek(0)
def print_a_line(line_count, f):
    print(line_count, f.readline())
        # We can add " end=' ' " at the end of this print command to not put an empty line between each print job


    # Prep our input_file for the functions
current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)

    # Without this next part, it won't print anything.
    # Currently we're on line 4 of the file.
print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)
    # This function below is redundant. Let's make it simpler next time.
current_line = current_line + 1
print_a_line(current_line, current_file)
    # The "+=" here adds to the current value of the variable by the dictated amount
current_line += 1
print_a_line(current_line, current_file)