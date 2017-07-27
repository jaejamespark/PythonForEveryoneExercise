import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup 
import re #import regular expression


URL = input('Enter the address: ')

html = urllib.request.urlopen(URL).read()
soup = BeautifulSoup(html, 'html.parser')


numbers = list()
tags = soup('span')
for tag in tags:
    number = tag.contents[0] #Takes the value of the span
    numbers.append(int(number))
    
    
#print(numbers)
print('Count ', len(numbers))
print('Sum ', sum(numbers))

