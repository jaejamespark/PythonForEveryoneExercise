import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup 
import re #import regular expression


URL = input('Enter the address: ')
scount = input('Enter count: ')
icount = int(scount)
sposition = input('Enter position: ')
iposition = int(sposition)
#URL='http://py4e-data.dr-chuck.net/known_by_Fikret.html'
link = URL
linklist = list()
linklist.append(link)

while icount > 0:
    html = urllib.request.urlopen(URL).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    i = 0
    for tag in tags:
        if i == iposition-1:
            link = tag.get('href', None)
            URL = link
            linklist.append(link)
        i = i + 1    
    icount = icount - 1        
    
for i in linklist:
    print('Retrieving: ', i)