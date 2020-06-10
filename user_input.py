            # 11: Asking Questions
    # end=' ' adds a space and tells the line to not skip down for the input
print("How old are you?", end=' ')
age = int(input())
    # int(input()) here turns the input into an integer instead of a string
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} years old, {height} tall, and you weigh {weight}lbs.")

print("What is your favorite hobby?", end=' ')
hobby = input()
print("What is the weather like right now?", end=' ')
weather = input()
print(f"It looks like the {weather} weather is good right now to {hobby}.")