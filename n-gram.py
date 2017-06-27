from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict

def cleanInput(input):
    input = re.sub('\n+', " ", input)
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +',  " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode('ascii', 'ignore')
    input = input.upper()
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput


def getNgrams(input, n):
    input = cleanInput(input)
    output = dict()
    for i in range(len(input)-n+1):
        newNGRam = ' '.join(input[i:i+n])
        if newNGRam in output:
            output[newNGRam] += 1
        else:
            output[newNGRam] = 1
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, 'html.parser')
content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
ngrams = getNgrams(content, 2)
ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))
print(ngrams)
print("2-grams count is: ", + str(len(ngrams)))
