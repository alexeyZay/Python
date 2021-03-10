import requests

url='https://earthquake.usgs.gov/fdsnws/event/1/query?'

starttime = input('Enter the start time: ')
endtime = input('Enter the end time: ')
latitude = input('Enter the latitude: ')
longitude = input('Enter the longitude: ')
maxradius = input('Enter the maxradius: ')
magnitude = input('Enter the magnitude: ')

response = requests.get(url,headers = {'Accept':'Application/json'},params={
    'format':'geojson',
    'starttime':starttime,
    'endtime':endtime,
    'latitude':latitude,
    'longitude':longitude,
    'maxradiuskm':maxradius,
    'minmagnitude':magnitude
    })

data = response.json()
quake_list=data['features']

count=0
for item in quake_list:
    count+=1
    print(f"{count}. Place: {item['properties']['place']}. MAgnitude: {item['properties']['mag']}")