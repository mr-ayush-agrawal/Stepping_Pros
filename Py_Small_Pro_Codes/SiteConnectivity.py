# This code checks the connetivity for any site

from urllib.request import urlopen

def url_check(url):
    print("Checking connectivity for", url)
    
    try:
        response = urlopen(url)
        print('The response code id',response.getcode(), end='\n\n')
    except :
        print('Error loading the site', end='\n\n')
    
test_urls= ['https://www.youtube.com', 'https://www.google.com', 'https://riotgames.com', 'https://github.com']
for link in test_urls:
    url_check(link)