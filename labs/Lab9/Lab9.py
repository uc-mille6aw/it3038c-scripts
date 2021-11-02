import json
import requests

r = requests.get('http://localhost:3000')
data = r.json()

length = len(data)
index_value = 0

while index_value < length:
    name = data[index_value]['name']
    color = data[index_value]['color']
    print('%s is %s.' % (name, color))
    index_value = index_value + 1

