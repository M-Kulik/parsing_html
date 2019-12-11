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
with webdriver.Chrome(options=options) as driver:
    # driver = webdriver.Chrome(options=options)
    driver.get(url)
    t1 = time.perf_counter()
    print('engaging browser: ' + str(round(t1, 2)) + 's')

    # list of all elements
    time.sleep(2)
    element = driver.find_elements_by_xpath('//*[not(child::*)]')
    all_elements = driver.find_elements_by_xpath('//div')

    t2 = time.perf_counter()
    print('collecting class tags: ' + str(round(t2, 2)) + 's')

    # getting element with most text in
    maxlen = element[0]
    print(maxlen.text)

    # # getting text in list
    # element_text = [a.text for a in element]
    # max_element = max(element_text, key=len)
    # print(max_element)
    # exit()

    for el in element:
        print(el)
        exit()
        if el.text is not None:
            if el.text > maxlen.text:
                maxlen = el

    t3 = time.perf_counter()
    print('getting longest text: ' + str(round(t3, 2)) + 's')

    # making list of all elements at the same position
    domlist = []
    for dom in element:
        doms = dom.location
        if doms.get('x') == maxlen.get('x'):
            domlist.append(dom)
            print(dom.text)
