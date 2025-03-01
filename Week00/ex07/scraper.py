import requests
import sys
import csv
from bs4 import BeautifulSoup

print(len(sys.argv))
if(len(sys.argv) != 2):
	print("Error Num of args")
	sys.exit()

try:
	r = requests.get('https://data.1337ai.org/')
	print("request return code ", r)
	print()
except:
	print("Error fetching this page")



soup = BeautifulSoup(r.content, 'html.parser')
#find table 
rows = soup.find_all('tr')
with open(sys.argv[1], 'w') as outfile:
	writer = csv.writer(outfile)
	for row in rows:
		row = [i .text for i in row]
		writer.writerow(row)
