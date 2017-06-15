import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html, "html.parser")
# The main comparison table is currently the fist table on the page
table = bsObj.findAll("table", {"class": "wikitable"})[0]
rows = table.findAll("tr")

csv_file = open("/home/christopher/Desktop/web_scraping/test.csv", 'w+')
writer = csv.writer(csv_file)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
            writer.writerow(csvRow)
finally:
    csv_file.close()
