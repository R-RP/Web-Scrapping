import requests
from bs4 import BeautifulSoup
import re
import urllib.request
#import pprint

res = requests.get('https://www.elections.tn.gov.in/GELS2014_Form20.aspx')
soup = BeautifulSoup(res.text,'html.parser')
tags = soup('a')
link = []
nu = []
for tag in tags:
	x = tag.get('href',None)
	final ='https://www.elections.tn.gov.in/'+ x 
	#if final.endswith(".pdf"):
	#	link.append(final)
	if re.search('[a-zA-Z]\d\d\d.pdf$',final):
		#y = re.findall('[a-zA-Z](\d\d\d).pdf$',final)
		#nu.append(int(y[0]))
		link.append(final)

#print(len(nu))
#print(len(link))
#print(link)	
#print(sorted(nu))

for url in link:
	#print(url)
	response = requests.get(url)
	name = re.findall('([a-zA-Z]*\d\d\d.pdf$)',url)
	#fname =name[0]
	urllib.request.urlretrieve(url,name[0])
	#with open(fname, 'wb') as f:		
	#	f.write(response.content)

print('Download Complete')

