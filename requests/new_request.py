import requests

url='https://earthquake.usgs.gov/fdsnws/event/1/query?'
#format=geojson&starttime=2014-01-01&endtime=2014-01-02
response = requests.get(url, headers = {'Accept':'Application/json'},params={
    'format':'geojson',
    'starttime':'2019-01-01',
    'endtime':'2019-05-01',
    'latitude':'51.51',
    'longitude':'-0.12',
    'maxradiuskm':'2000',
})

data = response.json()
#print(data.)
print(data['features'][1]['properties']['place'])