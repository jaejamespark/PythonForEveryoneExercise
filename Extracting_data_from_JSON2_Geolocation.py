import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'


while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    
    url = serviceurl + urllib.parse.urlencode({'address' : address})
    print('Retrieving ', url)
    
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved ', len(data), ' characters')
    info = json.loads(data)
    
   # print(json.dumps(info, indent=4))
    
    print('Place id', info['results'][0]['place_id'])




#  South Federal University