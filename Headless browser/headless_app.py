from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re

# SELENIUM WEBDRIVER
url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/#replace-with'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
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
lenght = []
for l in element:
    if l.text not in lenght:
        lenght.append(l.text)
maxlen = max(lenght, key=len)

t3 = time.perf_counter()
print('getting longest text: ' + str(round(t3, 2)) + 's')

# getting the element back
lentest = []
for elem in element:
    if elem.text == maxlen:
        lentest.append(elem)

t4 = time.perf_counter()
print('finding size: ' + str(round(t4, 2)) + 's')

# making list of all elements with max width
domlist = []
longest = lentest[0].size
for dom in element:
    doms = dom.size
    if doms.get('width') == longest.get('width'):
        if dom.text not in domlist:
            domlist.append(dom)

print(len(domlist))

exit()

# # # TODO: get width of element with most text, get all elements with same width
#
# # getting size width atribute of all dom elements
# size = [s.size for s in element]
# a = [x.get('width') for x in size]
# maxsize = max(a)
#
# # making list of all elements with max width
# domlist = []
# for dom in element:
#     doms = dom.size
#     if doms.get('width') == maxsize:
#         domlist.append(dom)
#
#
#
#
# exit()
# e = element[0].size
# print(e.get('width'))
# exit()
#
# print(test)
# exit()
# print(max([elem.size for elem in element.value]))
# exit()
# elelist = []
#
# for ele in element:
#     elelist.append(str(ele.get_property('width')))
#                    # .split("'width': ")[1].split('}')[0])
# print(elelist)
# widest = driver.find_elements_by_id('513')
# print(widest)
# exit()
# with open('elementlist.txt', 'w+') as f:
#     for ele in element:
#         f.write(str(ele.size))
#         f.write('\n')
# exit()
# # content = requests.get(url)
# soup = bs4.BeautifulSoup(content, 'html.parser')
# # for script in soup(["script", "style"]):
# #     script.extract()
#
# # getting all <p> tags
# tags = []
# for tag in soup.find_all('p', class_=False):
#     tags.append(tag)
#
# # getting all <p> tags parents
# ptags = []
# for ptag in tags:
#     if ptag.parent is not None:
#         if ptag.parent not in ptags:
#             ptags.append(ptag.parent)
#
# for tagt in ptags:
#     print(tagt.text)
#
# # TODO:
# #   PROBLEMS
# #   1. There is no spectfic class/id for all text sections,
# #   2. Text sections ar not on the same tree level,
# #   3. Text section tends to be in the same tag as side bars,
# #   4. DOM elements have no one size format,
# #   5. Text sections tends to be in biger DOM elements - can't chose section by size
# #   6. bs4 finds all p tags, separated parents
# #   7. Can't search for parent with most <p> tags, different parent tag division
# #   TRY
# #   1. Finding body by css size:
# #        -by padding
# #        -by px, %, vh;vw
# #
# #   getting all <p> tags and returning thier parents worked
#
# #
# # # works with first child
# # a = max(tags, key=len).text
# # print(a)
# # exit()
# # tags2 = []
# #
# #
# # print(tags2)
# # test = []
# # for tagg in tags:
# #     test.append(list([line for line in tagg.strings]))
# # hi = max(test, key=len)
# # print(test)
# #
# # hihi = max(hi, key=len)
# #
#     # SELENIUM WEBDRIVER
#     # options = webdriver.ChromeOptions()
#     # options.add_argument('--headless')
#     # options.add_argument('disable-gpu')
#     # driver = webdriver.Chrome(options=options)
#     # driver.get(adress)
#     # content = driver.page_source
# #
# # url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/#replace-with'
# #
# # content = requests.get(url)
# # soup = bs4.BeautifulSoup(content.content, 'lxml')
# # # for script in soup(["script", "style"]):
# # #     script.extract()
# #
# # # getting all <p> tags
# # tags = []
# # for tag in soup.find_all('p', class_=False):
# #     tags.append(tag)
# #
# # # getting all <p> tags parents
# # ptags = []
# # for ptag in tags:
# #     if ptag.parent is not None:
# #         if ptag.parent not in ptags:
# #             ptags.append(ptag.parent)
# #
# # for tagt in ptags:
# #     print(tagt.text)
