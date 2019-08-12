import urllib.request, urllib.parse, urllib.error
import bs4
from pathlib import Path
import html2text
import os
import http
from http import cookiejar

url_list_dir = "C:/Users/Mateusz/Documents/Python programy/Upraszczanie stron/Pliki zewnętrzne/"
url_list_file = "url_list.txt"
file_dir = os.path.join(f"{url_list_dir}{url_list_file}")
# directing to url_list

try:
    with open(file_dir, "r") as a:
        exc_1 = a.read()
except FileNotFoundError:
    print("error: check urllist filename; file has to have .txt extension")
    exit()
    # handling wrong urllist file extension

with open(file_dir) as fp:
    lines = [ line for line in fp.readlines() if line.strip()]

    if len(lines)<3:
        print("error: no url in line")
        exit()
    # handling empty lines

    line_count = len(lines)
    c = 0
    # counting lines for loop

    while c < line_count:
        scrapped_dir = os.path.join("C:/Users/Mateusz/Documents/Python programy/Upraszczanie stron/Pliki zewnętrzne/scrapped/")

        url_line = lines[c]
        if url_line.startswith("https://") or url_line.startswith("http://"):
            url = url_line
        else:
            url = "http://"+url_line
        # taking care of wrong url format

        try:
            r = urllib.request.urlopen(url)
        except urllib.error.URLError as e:
            print(e)
            # handle wrong url exception

        search_name = url.replace(".", "_").replace("/", "-").replace(":", "^").rstrip()
        # replacing characters incompatible with windows file saving

        if os.path.exists(scrapped_dir + search_name + ".txt") is True:
            with open(scrapped_dir + search_name + ".txt", encoding="utf-8") as file:
                file_is = file.read()
                print(url + "Webpage oppened from file")
                c += 1
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
            print(url + " saved to file")
            # changing url network location to proper file name

            with open(scrapped_dir + search_name + ".txt", "w+", encoding="utf-8") as f:
                f.write(no_html)
            # saving text file with cleared web page

            c += 1