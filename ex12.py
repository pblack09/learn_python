            # 12: Prompting People
    # Does the same as ex.11 with less lines of code
age = int(input("How old are you? "))
    # Age is now collected as an integer from the user
height = input("How tall are you? ")
weight = input("How much do you weigh? ")
    # Prints the same as ex.11
print(f"So, you're {age} years old, {height} tall, and weigh {weight}lbs.")
print("In 5 years, you'll be ", age + 5, " years old.")
    # Below will put the input before the prompt.
    # It needs to be sequenced AFTER the prompt with a comma.
print("How old are you?" , input())
print("How old are you?"), input()