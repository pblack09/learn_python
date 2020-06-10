            # 18: Names, Variables, Code, Functions
            
    # "*args"  stands for   "list"  which is defined on the next line by "args = arg1, arg2"
    # This is redundant
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
    
    # This is the normal way to write functions
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}:")

def print_none():
    print("I got nothin'.")

print_two("Philip", "Black")
print_two_again("Philip", "Black")
print_one("Alone")
print_none()