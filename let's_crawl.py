from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("https://frombitstobytes.com/about/")
bsObj = BeautifulSoup(html, 'html.parser')
for link in bsObj.findAll("a"):
    if 'href' in link.attrs:  # attrs <- accessing attributes
        # dictionary object
        print(link.attrs['href'])
