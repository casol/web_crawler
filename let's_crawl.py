from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import datetime
import re
import random

random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    try:
        html = urlopen("http://en.wikipedia.org"+articleUrl)
    except HTTPError as err:
        return None
    try:
        bsObj = BeautifulSoup(html, "html.parser")
        page_links = bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
    except AttributeError as err:
        return None
    return page_links

links = getLinks("/wiki/Kevin_Bacon")
if links is None:
    print('Page or tag could not be found')
else:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
        print(newArticle)
        links = getLinks(newArticle)
