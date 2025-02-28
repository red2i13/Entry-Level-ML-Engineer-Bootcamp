import requests
import sys
from bs4 import BeautifulSoup



r = requests.get('https://data.1337ai.org/')
print("request return code ", r)
print()


soup = BeautifulSoup(r.content, 'html.parser')

[print (item.prettify()	) for item in soup.find_all('table')]