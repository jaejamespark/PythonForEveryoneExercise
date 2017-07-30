import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup 
import re #import regular expression
import ssl

# Ignore SSL certificate error for https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#URL = input('Enter the address: ')

URL = 'https://www.glassdoor.com/'
#URL ='http://py4e-data.dr-chuck.net/'

req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
opener = urllib.request.build_opener()
reponse = opener.open(req)
html = urlopen(reponse).read()

soup = BeautifulSoup(html, 'html.parser')
print(soup)


from urllib.request import Request, urlopen

#req = Request('http://www.cmegroup.com/trading/products/#sortField=oi&sortAsc=false&venues=3&page=1&cleared=1&group=1', headers={'User-Agent': 'Mozilla/5.0'})
#webpage = urlopen(req).read()