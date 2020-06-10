from sys import argv
script, in_file = argv

edit = open(in_file, 'w')
edit.write("""
Here is some sample text.\n
Hopefully this works...
""")
           
print(edit)

edit.close()