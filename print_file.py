from sys import argv
script, filename = argv

txt = open(filename)

print("Now opening desired file...")
print(txt.read())