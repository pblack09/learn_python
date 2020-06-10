            #10: What Was That?
    # \t tabs over 1
    # \n goes to a new line
    # \\ is how you write 1 \ in a string in case needed
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

format1 =  "{} {}"
print(format1.format("This is\na test.", "\tWhat if I add a tab?"))