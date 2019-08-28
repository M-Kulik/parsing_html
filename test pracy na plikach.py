import urllib.request, urllib.parse, urllib.error
import bs4
import os

url_list_dir = "C:/Users/Mateusz/Documents/Python programy/Upraszczanie stron/Pliki zewnętrzne/"
url_list_file = "url_list.txt"
scrapped_dir = os.path.join("C:/Users/Mateusz/Documents/Python programy/Upraszczanie stron/Pliki zewnętrzne/scrapped/")

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
    line = fp.readlines()
    line_count = len(line)
    c = 0
# counting lines for loop

    while c < line_count:
# directing to scrapped websites folder

        url_line = line[c]
        if len(url_line) < 3:
            print("error: no url in line")
            exit()
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
# replacing characters incompatible with windows file saving format

        if os.path.exists(scrapped_dir + search_name + ".txt") is True:
            with open(scrapped_dir + search_name + ".txt", encoding="utf-8") as file:
                file_is = file.read()
                print(url + "Webpage opened from file")
                c += 1
# printing content if present in storage folder

        else:
            soup = bs4.BeautifulSoup(r, 'html.parser')
            for script in soup(["script", "style"]):
                script.extract()
# removing scripts and hidden text

            with open(scrapped_dir + search_name + ".txt", "w+", encoding="utf-8") as f:
                raw_text = soup.get_text()
                f.write(raw_text)
# saving soup in raw text form

                f.seek(0)
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if i.find("ookie") or ("ciasteczka") or ("ciasteczek") == -1:
                        f.write(i)
                f.truncate()
                f.seek(0)
                text_no_cookies = f.read()
                f.truncate(0)
# taking care of cookies popups

                lines = (line.strip() for line in text_no_cookies.splitlines())
                chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                text = '\n'.join(chunk for chunk in chunks if chunk)
                f.write(text)
                print(text)
# converting text to more readable form

            c += 1
