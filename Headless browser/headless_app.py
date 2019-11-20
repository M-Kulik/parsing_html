from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bs4
import urllib.request, urllib.error
import time
from flask import Flask
import html2text

adress = r'https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python'
url = urllib.request.urlopen(adress)

soup = bs4.BeautifulSoup(url, 'html.parser')
for script in soup(["script", "style"]):
    script.extract()

# getting all <p> tags
tags = []
for tag in soup.find_all('p', class_=False):
    tags.append(tag)

# getting all <p> tags parents
ptags = []
for ptag in tags:
    if ptag.parent is not None:
        if ptag.parent not in ptags:
            ptags.append(ptag.parent)

for tagt in ptags:
    print(tagt.text)

exit()
# TODO:
#   PROBLEMS
#   1. There is no spectfic class/id for all text sections,
#   2. Text sections ar not on the same tree level,
#   3. Text section tends to be in the same tag as side bars,
#   4. DOM elements have no one size format,
#   5. Text sections tends to be in biger DOM elements - can't chose section by size
#   6. bs4 finds all p tags, separated parents
#   7. Can't search for parent with most <p> tags, different parent tag division
#   TRY
#   1. Finding body by css size:
#        -by padding
#        -by px, %, vh;vw


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
