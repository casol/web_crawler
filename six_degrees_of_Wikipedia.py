from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='22listopad',
                       db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute("USE wikipedia")


def insert_page_if_not_exist(url):
    cur.execute("SELECT * FROM pages WHERE url = %s", (url))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO pages (url) VALUES (%s)", (url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]


def insert_link(fromPageId, toPageId):
    cur.execute("SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s",
                (int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO links (fromPageId, toPageId) VALUES (%s, %s)",
                    (int(fromPageId), int(toPageId)))
        conn.commit()

pages = set()


def get_links(pageUrl, recusionLevel):
    global pages
    if recusionLevel > 4:
        return;
    pageId = insert_page_if_not_exist(pageUrl)
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html, 'html.parser')
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        insert_link(pageId, insert_page_if_not_exist(link.attrs['href']))
        if link.attrs['href'] not in pages:
            # We have encountered a new page, add it and search it for links
            newPage = link.attrs['href']
            pages.add(newPage)
            get_links(newPage, recusionLevel+1)

get_links("/wiki/Kevin_Bacon", 0)
cur.close()
conn.close()