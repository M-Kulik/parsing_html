from flask import Flask
import os
import bs4
import urllib.parse, urllib.error, urllib.request

# Init app
app = Flask(__name__)


# url of scrapped page
# url = r"https://www.pipeburn.com/home/2019/09/09/titanium-tracker-ecosse-heretic-by-roland-sands-designs.html"

# file related variables

# app route and access method
@app.route('/<path:url>', methods=['GET'])
def getfile(url):

    scrapped_dir = os.path.join("C:/Users/Mateusz/PycharmProjects/parsing_html/Pliki zewnętrzne/scrapped/")
    search_name = urllib.parse.quote_plus(url)
    filename = os.path.join(scrapped_dir + search_name + ".txt")
    url_path = urllib.parse.quote(url, safe='')

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

        # removing scripts
        for script in soup(["script", "style"]):
            script.extract()

        # creating file to store text
        with open(filename, "w+", encoding='utf-8') as f:
            raw_text = soup.get_text()
            linelist = []

            # removing cookie popups
            for i in raw_text.splitlines():
                if i.find("ookie" or "ciasteczka" or "ciasteczek") == -1:
                    linelist.append(i)

            # removing white spaces and null characters from lines
            chunks = (phrase.strip().strip('\x00') for line in linelist for phrase in line.split("  "))

            # saving as string to file
            file_new = '\n'.join(chunk for chunk in chunks if chunk)
            f.write(file_new)
            return file_new



# running flask server from this script
if __name__ == '__main__':
    app.run(debug='True')