# print(type("hello"))
#
#
# def apply(f, x):
#    return f(x)
#
# apply(lambda x: x * 3, 10)
#
# doubles = []
# l = range(10)
# for element in l:
#     doubles.append(element * 2)
#
# doubles2 = []
#
# doubles2 = list(map(lambda x: x * 2, l))
# print(doubles2)
import time
import time
import urllib.request as rq
import urllib.request, json
import requests
from lxml import html, cssselect

import cssselect

#
# url = "http://www.google.com"
# tem = (str(rq.urlopen(url).read()))
# for ele in tem:
#     print (ele)

# print(url, (str(rq.urlopen(url).read())))


# urls = [
#     'https://www.indeed.com/',
#     'http://www.python.org/about/'
# ]


def single_fetch():
    page = requests.get("http://www.example.com").text
    doc = html.fromstring(page)
    print(doc.txt)

    link = doc.cssselect("a")[0]
    print(link.text_content())
    # More information...
    print(link.attrib['href'])
    # http://www.iana.org/domains/example

single_fetch()

