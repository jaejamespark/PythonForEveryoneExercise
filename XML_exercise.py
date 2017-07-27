import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

URL = input('Enter location: ')
print('Retrieving ', URL)

data = urllib.request.urlopen(URL).read()
tree = ET.fromstring(data)
print('Retrieved: ', len(data), 'characters')

counttag = tree.findall('.//count')
print('Count: ', len(counttag))

sum = 0
for eachcount in counttag:
    count = eachcount.text
    sum = sum + int(count)

print('Sum: ', sum)