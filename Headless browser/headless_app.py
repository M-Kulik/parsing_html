from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bs4
import time

# SELENIUM WEBDRIVER
url = r'https://www.w3schools.com/xml/xpath_axes.asp'
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('disable-gpu')
with webdriver.Chrome(options=options) as driver:
    driver.get(url)
    time.sleep(2)
    t1 = time.perf_counter()
    print('browser: ' + str(round(t1, 2)))
    # driver.implicitly_wait(10)

    # list of all elements
    # //*[not (child::*)] - tag in any place with no children
    element = driver.find_elements_by_xpath('//*[not (child::*)]')
    element2 = driver.find_elements_by_xpath('//div[not (@id="footer")]')
    te = time.perf_counter()
    print('element: ' + str(round(te, 2)))

    '''
    **finding div closest to maxlen and printing ONLY it
    getting all the tegs with same position, if tag not in tag.children append
    
    '''
    # conten = driver.find_elements(By.XPATH, '//*')
    maxlen = element[0]

    for e in element:
        if e.text is not None:
            if len(e.text) > len(maxlen.text):
                maxlen = e
    t2 = time.perf_counter()
    print('longest text: ', str(round(t2, 2)))

    maxloc = maxlen.location
    xloc = maxloc.get('x')
    print(xloc)
    t3 = time.perf_counter()
    print('location: ' + str(round(t3, 2)))

    # list of elements at THE location
    for el in element2:
        if el.location.get('x') == xloc:
            print(el.text)
