from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bs4
import urllib.request, urllib.error
import time
from flask import Flask
import html2text

adress = r'http://127.0.0.1:5000/website'
url = urllib.request.urlopen(adress)

soup = bs4.BeautifulSoup(url, 'lxml-xml')

for script in soup(["script", "style"]):
    script.extract()

# contents of body
tags = []
for kid in soup.body.contents:
    if kid.name is not None:
        tags.append(kid)

# TODO:
#   1. There is no spectfic class/id for all text sections,
#   2. Text sections ar not on the same tree level,
#   3. Text section tends to be in the same tag as side bars,
#   4. DOM elements have no one size format

# works with first child
a = max(tags, key=len).text
print(a)
exit()
tags2 = []


print(tags2)
test = []
for tagg in tags:
    test.append(list([line for line in tagg.strings]))
hi = max(test, key=len)
print(test)

hihi = max(hi, key=len)

    # SELENIUM WEBDRIVER
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome()
# driver.get(adress)
# content = driver.page_source
# options.add_argument('--headless')
# options.add_argument('disable-gpu')
