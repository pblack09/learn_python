    # Making Lists, Checking Them Twice
first_list = "1 2 3 4 5 6"
print(first_list)
stuff = first_list.split()
print("Split: (Split into separate objects)", stuff)
reverseStuff = stuff.reverse()
print(reverseStuff)
more_stuff = ["14", "13", "12", "11", "10", "9", "8", "7"]
print()

    # List Functions
stuff.append('Add')
print("Append: (Add at end)", stuff)
stuff.count('11')
print("Count: ", stuff.count('11'), "<-- # of times '11' appears in list")
stuff.extend(more_stuff)
print("Extend: ", stuff)
stuff.index('4')
print("Index: ", stuff.index('4'), "<-- Show where '4' is in the list")
stuff.insert(3, 'Insert')
print("Insert: (Insert at given index)", stuff)
stuff.pop()
print("Pop: (Move or remove last item)", stuff)
stuff.remove('3')
print("Remove: (Remove given object)", stuff)
print(stuff)
stuff.reverse()
print("Reverse: ", stuff)
stuff.sort()
print("Sort: **Notice how it sorts #s by characters when strings**", stuff)
print()

    # List Values
len(stuff)
print("Length: (Length of list)", len(stuff))
max(stuff)
print("Max: (Highest value from list)", max(stuff))
min(stuff)
print("Min: (Lowest value from list)", min(stuff))
print()

    # Translate to List
test_tuple = ("test1", "test2", "test3")
print(test_tuple)
new_list = list(test_tuple)
print("Turn Tuple into a List: ", new_list)
