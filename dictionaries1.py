      # 39: Dictionaries

states = {
  'Oregon': 'OR',
  'Florida': 'FL',
  'Texas': 'TX',
  'Wyoming': 'WY',
  'Nevada': 'NV'
}

cities = {
  'OR': 'Portland',
  'TX': 'Dallas',
  'WY': 'Cheyenne',
}

    # states = ['Oregon' = 'OR']; cities = ['OR' = 'Portland']
    # states[cities['Portland']] = ['Portland' = 'OR' = 'Oregon']
    #   ^Finds the states of the given {cities}
    # cities[states['Oregon']] = ['Oregon' = 'OR' = 'Portland']
    #   ^Finds the cities of the given {states}

cities['NV'] = 'Las Vegas'
cities['FL'] = 'Miami'

print('-'*10)
print("TX State has: ", cities['TX'])
print("NV State has: ", cities['NV'])

print('-'*10)
print("Miami is located in: ", states['Florida'])
print("Wyoming's abbreviation is: ", states['Wyoming'])

print('-'*10)
print("Oregon has: ", cities[states['Oregon']])
print("Texas has: ", cities[states['Texas']])

print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print('-'*10)
for abbrev, city in list(cities.items()):
    print(f"{city}, {abbrev}")

print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} is labeled as {abbrev} and has the city of {cities[abbrev]}.")

print('-'*10)
state = states.get('Oklahoma')

if not state:
    print("Sorry, no Oklahoma.")

print('-'*10)
city = cities.get('OK', 'Does Not Exist')
print(f"The city for the state of 'OK' is: {city}.")
