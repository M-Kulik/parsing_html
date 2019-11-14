from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bs4
import urllib.request, urllib.error
import time
from flask import Flask
import html2text

url = urllib.request.urlopen('http://127.0.0.1:5000/website')
# off = open('random_website.html', 'r', encoding='utf-8')
soup = bs4.BeautifulSoup(url, 'lxml-xml', from_encoding='utf-8')

tags = []

for kid in soup.body.contents:
    if kid.name is not None:
        tags.append(kid)


test = []
for tagg in tags:
    test.append(list([line for line in tagg.strings]))
hi = max(test, key=len)
print(hi)


#  tree traverse #1
# first_run = soup.body.children
# for kid in first_run:
#     if kid.name is not None:
#         for kid2 in kid.children:
#             print(kid2)
# root_childs = [e.name for e in first_run if e.name is not None]
# body_divs = [soup.body.child for e in soup.body.child if e.name is not None]
# # for e in soup.body.children:
# #     body_divs.append(e)
#
# print(body_divs)
# print(root_childs)
# root_childs2 = []
# for child in root_childs:
#     print(child)
