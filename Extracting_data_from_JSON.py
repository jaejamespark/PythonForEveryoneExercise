import urllib.request, urllib.parse, urllib.error
import json



while True:
    url = input('Enter location: ')
    if len(url) < 1: break
    print('Retrieving ', url)
    
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved ', len(data), ' characters')
    info = json.loads(data)
    
    countlist = list()
    print(json.dumps(info, indent=4))
    
    for item in info['comments']:
        count = item['count']
        countlist.append(int(count))
        
    print('Count: ', len(countlist))
    print('Sum: ', sum(countlist))


# http://py4e-data.dr-chuck.net/comments_42.json