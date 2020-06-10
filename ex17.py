            # 17: More Files

#from sys import argv
#from os.path import exists

#script, from_file, to_file = argv

#print(f"Copying from {from_file} to {to_file}.")

#indata = open(from_file).read()

#print(f"The input file is {len(indata)} bytes long.")

#print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()

#out_file = open(to_file, 'w')
#out_file.write(indata)

#print("Alright, all done.")

#out_file.close()

    # Shorter version written below

from sys import argv
script, from_file, to_file = argv
indata = open(from_file).read()
outdata = open(to_file, 'w')
outdata.write(indata)
print("Done.")

    # You can write back-to-back commands on one line
    # by separating them with a semi-colon
    # ex) from sys import argv; script, from_file, to_file = argv; indata = open(from_file).read()