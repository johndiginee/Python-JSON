import json

# Loading JSON
with open('states.json') as f:
    data = json.load(f)

# Looping through JSON
for state in data['states']:
    print(state)
# Looping through JSON name and abbreviation only
for state in data['states']:
    print(state['name'], state['abbreviation'])

# Removing keys from JSON
for state in data['states']:
    del state['area_codes']

with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)