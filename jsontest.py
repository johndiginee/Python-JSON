import json

people_string = '''
{
    "people": [
        {
            "name": "John Smitch",
            "phone": "506-454-2234",
            "emails": ["john@gmail.com", "james@gmail.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "545-564-5644",
            "emails": null,
            "has_license": true
        }
    ]
}
'''
# Convert json to python
data = json.loads(people_string)

#printing json objects
for people in data['people']:
    print(people['name'])

#deleting json data
for people in data['people']:
    del people['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)

print(new_string)