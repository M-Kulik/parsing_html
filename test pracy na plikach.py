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
    print(line_count)
    # count lines for loop

    while c < line_count:
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

        soup = bs4.BeautifulSoup(r, 'html.parser')
        clean = soup.prettify()
        # feeding soup with html code

        no_html = html2text.html2text(clean)
        encoded_html = no_html.encode("utf-8")

        # getting plain text from soup

        domain = urllib.parse.urlparse(url)
        netloc = domain.netloc
        plain_url = netloc.strip()
        file_name = plain_url.replace(".", "_")
        print(file_name)
        # changing url network location to proper file name

        os.chdir("C:\\Users\\Mateusz\\Documents\\Python programy\\Upraszczanie stron\\Pliki zewnętrzne\\scrapped")
        text_file = open(file_name+".txt", "w+")
        text_file.write(encoded_html.__str__())
        text_file.close()
        # saving text file with cleared webpage
        print("success!")
        c += 1

