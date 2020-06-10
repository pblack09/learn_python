            # 14: Prompting and Passing
from sys import argv
script, user_name = argv
    # '>' adds a > at the start of the line where the user answers the prompt "var1"
var1 = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me, {user_name}?")
likes = input(var1)

print(f"Where do you live {user_name}?")
lives = input(var1)

print(f"What kind of computer do you have?")
computer = input(var1)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice!
""")