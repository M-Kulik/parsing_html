import os
import urllib.request, urllib.parse, urllib.error
import requests
import bs4
from pathlib import Path, PureWindowsPath

######### ZNAKI ZAKAZANE \/:*?"<>| ########

file_dir = Path("C:/Users/Mateusz/Documents/Python programy/Upraszczanie stron/Pliki zewnętrzne/url_list.txt")
# feeding url list file directory

with open(file_dir) as fp:
    line = fp.readlines()
    line_count = len(line)
    c = 0
# count lines for loop

    while c < line_count:
        url = line[c]
        if not urllib.parse.urlparse(url).scheme:
            print("error: invalid url (use http:// format)")
            break
# handle wrong url format exception

        try:
            r = urllib.request.urlopen(url)
        except urllib.error.URLError as e:
            print(e)
            break
# handle wrong url exception

        soup = bs4.BeautifulSoup(r, 'html.parser')
        nazwa_pliku = soup.title.text  #URL

        body = soup.body
        print(body.text)
        # for paragraph in body.find_all('p'):
        #     print(paragraph.text)
        #     p_zewn = open('blablabla' + '.txt', '+w')
        #     p_zewn.write(paragraph.text)



        # print(znaczniki)
        # tekst = znaczniki.text
        # print(tekst)
        # p_wyjsciowy = open(nazwa_pliku, 'w+')



        c += 1
#
# linie = f.readlines()
# ilosc_stron = len(linie)
# i = 0
# url = linie[i]
#
# r = requests.get(url)`
# print(r.text)
#


# while i < ilosc_stron:
#     soup = BeautifulSoup(linie[i], 'html.parser')
#     print(soup.prettify())
#     i = i+1
#

# while i<ilosc_stron:
#     print(linie[i])
#     i=i+1
#
