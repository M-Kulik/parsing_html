from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re

# SELENIUM WEBDRIVER
url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/#replace-with'
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('disable-gpu')
driver = webdriver.Chrome(options=options)
driver.get(url)
t1 = time.perf_counter()
print('engaging browser: ' + str(round(t1, 2)) + 's')

# list of all elements
element = driver.find_elements_by_xpath('//*[@id]')
content = driver.page_source

t2 = time.perf_counter()
print('collecting class tags: ' + str(round(t2, 2)) + 's')

# getting element with most text in
# lenght = [l.text for l in element if l.text not in lenght]
# lenght = []
maxlen = 0

for l in element:
    tlen = maxlen + 1
    if tlen > maxlen:
        maxlen = tlen

t3 = time.perf_counter()
print('getting longest text: ' + str(round(t3, 2)) + 's')

exit()

# getting the element back
lentest = []
for elem in element:
    if elem.text == maxlen:
        lentest.append(elem)

# making list of all elements with max width
domlist = []
longest = lentest[0].size
for dom in element:
    doms = dom.size
    if doms.get('width') == longest.get('width'):
        if dom.text not in domlist:
            domlist.append(dom)
            print(dom.text)
