high_schools = {
  'Centennial': 'Titans',
  'Liberty': 'Redhawks',
  'Wakeland': 'Wolverines',
  'Lone Star': 'Cowboys'
}

    # Print the school's mascot.
print(high_schools['Centennial'])

print('-'*10)

frisco = {
    'East': 'Centennial',
    'West': 'Wakeland',
    'East': 'Liberty',
    'West': 'Lone Star'
}
    # Assigning the same 'key' or 'value' overwrites the first one.
print(frisco['West'])
print(frisco['Liberty'])
#print(frisco[1]) Produces a KeyError

print('-'*10)

numbers = {
    1: 10 + 1,
    2: 1 + 4,
    3: '2 + 20',
    4: 2 + 9
}

print(numbers[2])
print(numbers[1+2])
    # Feeds back the value for '3' which is '2 + 20'
    # Only works if 1 and 2 are in the dict; 1 and '2' gives an error

print('-'*10)

animals = {
    'Cat': 'Feline',
    'Dog': 'Canine',
    'Beetle': 'Insect',
    'Trout': 'Fish',
    'CatDog': 'Cartoon'
}

print(animals['Cat'+'Dog'])
    # Prints the value for 'CatDog' which is 'Cartoon'
    # How could this be useful?

print('-'*10)

frisco = ['Centennial', 'Liberty', 'Reedy', 'Independence']
lewisville = ['Hebron', 'Flower Mound', 'Marcus']
leander = ['Leander', 'Cedar Park', 'Vandegrift']

uil = {
    'Region 24': frisco,
    'Region 2': lewisville,
    'Region 16': leander
}

print(uil['Region 24']) #Prints the list for frisco
#print(uil['Region 24', 'Region 2']) Kicks back a KeyError
print(uil['Region 24'][1])  #Prints index 1 for the list frisco
uil['Region 24'].sort()
print(frisco)   #Order of the list has now been sorted
uil['Region 24'].extend(uil['Region 2'])
print(frisco)   #^Same as frisco.extend(lewisville)
print(lewisville)   #List is still there
