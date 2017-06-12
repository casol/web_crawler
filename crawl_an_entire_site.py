"""
Crawling an entire site, without duplicate links and
collecting data. Printing title and first paragraph and then
moving to the next site.
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()


def getLinks(pageUrl):
    global pages
    html = urlopen("http://pl.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html, 'html.parser')
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0].get_text())
        #print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing something! No worries though!")

    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # New page
                newPage = link.attrs['href']
                print("-----------\n"+newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks("/wiki/Grenada_(miasto_w_Hiszpanii)")

