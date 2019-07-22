import os
import urllib.request
import requests
import bs4
from urllib import parse

######### ZNAKI ZAKAZANE \/:*?"<>| ########

cwd = os.getcwd()
print(cwd)
list_dir = 'url_list.txt'

with open(list_dir) as fp:
    line = fp.readlines()
    c = 0
    line_count = 4

    while c < line_count:
        url = line[c]
        try:
            r = urllib.request.urlopen(url)
            break
        except:
            print(sys.exc_info()[0], 'error, wrong url')
            # handle exception here

        soup = bs4.BeautifulSoup(r, 'html.parser')

        print(soup)
        nazwa_pliku = soup.title.text  #URL
        body = soup.body
        for paragraph in body.find_all('p'):
            print(paragraph.text)
            p_zewn = open('blablabla' + '.txt', '+w')
            p_zewn.write(paragraph.text)

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
# r = requests.get(url)
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
