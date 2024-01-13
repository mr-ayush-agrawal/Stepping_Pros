# Extracting data from the websotes

import requests
from bs4 import BeautifulSoup

url = 'https://www.coursera.org/professional-certificates?trk_ref=camodule'
r = requests.get(url)
print()
Soup = BeautifulSoup(r.content)

title = Soup.find_all('p', {'class': 'cds-119 cds-Typography-base css-j2b34a cds-121'})
for l in title:
    print(l.getText(), end='\n')
print(type(title))
