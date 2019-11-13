from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bs4
import urllib.request, urllib.error
import time


# TODO:
'''
1. DONE Bs4 list all of body children
2. list all children of (1)children
3. Search for tag with most of text
'''


# url engaging
# url = r'https://pl.wikipedia.org/wiki/Filmografia_Grety_Garbo'
# r = urllib.request.urlopen(url)

# # getting conent with selenium
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(options=chrome_options)
# driver.get(url)
# time.sleep(5)
# content = driver.page_source.encode('utf-8').strip()

# offline html file

off = open('wikihtml.txt', 'r', encoding='utf-8')
soup = bs4.BeautifulSoup(off.read(), 'html.parser')

#  tree traverse #1
first_run = soup.body.children
for kid in first_run:
    if kid.name is not None:
        for kid2 in kid.children:
            print(kid2)
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
exit()
#       RENAMING TAGS
# c = 0
# for kid in soup.body.children:
#     if kid.name is not None:
#         old_tag = soup.kid
#         new_tag = soup.new_tag(f'{old_tag}{c}')
#         try:
#             old_tag.replace_with(new_tag)
#         except AttributeError as e:
#             pass
#             c += 1
#
#
# # tree traverse #2
# renamed = [e.name for e in soup.body.children if e.name is not None]
# print(soup)
# # tags2 = [tag2.children for tag2 in renamed]

# removing scripts
for script in soup(["script", "style"]):
    script.extract()


# finding cookies


# r = re.compile('.*ookie.*')
# newlist = list(filter(r.match, spara))
# print(newlist)


# for line in spara:
#     if not re.compile(r'.cookie', line):
#         plist.append(line)


# # creating file to store text
# raw_text = soup.get_text()
#
# # removing cookie popups
# for i in raw_text.splitlines():
#     if i.find("ookie" or "ciasteczka" or "ciasteczek") == -1:
#         linelist.append(i)
#
# # removing white spaces and null characters from lines
# chunks = (phrase.strip().strip('\x00') for line in linelist for phrase in line.split("  "))
#
# # saving as string to file
# file_new = '\n'.join(chunk for chunk in chunks if chunk)
# print(file_new)
