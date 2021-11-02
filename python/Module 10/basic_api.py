import json
import requests

print('Please enter your zip code:')
zip = input()

r = requests.get('https://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=935a1ece2120d4893db52359dd21d5e0' % zip)
data = r.json()
print(data['weather'][0]['description'])