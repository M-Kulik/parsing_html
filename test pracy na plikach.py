import urllib.request, urllib.parse, urllib.error
import requests
import bs4
from pathlib import Path, PureWindowsPath
import html2text
from http import cookiejar
import json
import tldextract
import os

######### ZNAKI ZAKAZANE \/:*?"<>| ########

file_dir = Path("C:/Users/Mateusz/Documents/Python programy/Upraszczanie stron/Pliki zewnętrzne/url_list.txt")
# feeding url list file directory

with open(file_dir) as fp:
    line = fp.readlines()
    line_count = len(line)
    c = 0
    # count lines for loop

    while c < line_count:
        os.chdir("C:\\Users\\Mateusz\\Documents\\Python programy\\Upraszczanie stron\\Pliki zewnętrzne\\scrapped")

        url_line = line[c]
        if url_line.startswith("https://") or url_line.startswith("http://"):
            url = url_line
        else:
            url = "http://"+url_line
        # taking care of wrong url format

        try:
            r = urllib.request.urlopen(url)
        except urllib.error.URLError as e:
            print(e)
            break
            # handle wrong url exception

        search_name = url.replace(".", "_").replace("/", "-").replace(":","^")
        # replacing characters incompatible with windows file saving

        if os.path.exists(search_name + ".txt") is True:
            with open(search_name + ".txt", encoding="utf-8") as file:
                file_is = file.read()
                print(file_is)
                c+=1
        # printing content if present in storage folder
        else:
            soup = bs4.BeautifulSoup(r, 'html.parser')
            clean = soup.prettify()
            # feeding soup with html code

            no_html = html2text.html2text(clean)
            # getting plain text from soup

            domain = urllib.parse.urlparse(url)
            netloc = domain.netloc
            plain_url = netloc.strip()
            file_name = plain_url.replace(".", "_")
            print("url: " + url)
            print("file name: " + search_name)
            # changing url network location to proper file name

            with open(search_name + ".txt", "w+", encoding="utf-8") as f:
                f.write(no_html)
                print("Done boss!")
            # saving text file with cleared webpage

            print("\nsaving successful!" + "\n_______________________________")
            c += 1

