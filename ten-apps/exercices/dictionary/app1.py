import json

data = json.load(open('data.json'))
print(type(data))
print(type(data['rain']))
print(data['rain'])
