from flask import Flask
import os
import bs4
import urllib.parse, urllib.error, urllib.request

# Init app
app = Flask(__name__)


# url of scrapped page
url = r"https://www.pipeburn.com/home/2019/09/09/titanium-tracker-ecosse-heretic-by-roland-sands-designs.html"

# file related variables
scrapped_dir = os.path.join("C:/Users/Mateusz/PycharmProjects/parsing_html/Pliki zewnętrzne/scrapped/")
search_name = urllib.parse.quote_plus(url)
filename = os.path.join(scrapped_dir + search_name + ".txt")


# app route and access method
@app.route('/getfile', methods=['GET'])
def getfile():

    # handling http status codes
    try:
        urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        return str(e)

    # checking if file in folder
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            file_open = f.read()
            # stripping null bytes from top of txt file
            return file_open.strip('\x00')
    else:
        r = urllib.request.urlopen(url)
        soup = bs4.BeautifulSoup(r, 'html.parser')

        # extracting all script tags
        for script in soup(["script", "style"]):
            script.extract()

        # saving file
        with open(filename, "w+", encoding='utf-8') as f:
            raw_text = soup.get_text()
            f.write(raw_text)
            f.seek(0)
            d = f.readlines()
            f.truncate(0)

            # removing cookie policy popup text
            for i in d:
                if i.find("ookie" or "ciasteczka" or "ciasteczek") == -1:
                    f.write(i)

            f.seek(0)
            text_no_cookies = f.read()
            f.truncate(0)

            # striping file into lines
            lines = (line.strip() for line in text_no_cookies.splitlines())

            # removing white spaces and null characters from lines
            chunks = (phrase.strip().strip('\x00') for line in lines for phrase in line.split("  "))

            # removing empty lines and saving as string to file
            file_new = '\n'.join(chunk for chunk in chunks if chunk)
            f.write(file_new)
            return file_new


getfile()

# running flask server from this script
if __name__ == '__main__':
    app.run(debug='True')
