from flask import Flask, request, jsonify
import os,bs4
import urllib.parse, urllib.request

# Init app
app = Flask(__name__)

# TODO:
# remove \"\\x00\\x00\\x00\\x00\\x00 from begeinig of file,
# printing array in more readable form


@app.route('/', methods=['GET'])
def text():
    return "hello dumbass"


url = r"https://docs.python.org/3/library/urllib.parse.html"
scrapped_dir = os.path.join("C:/Users/Mateusz/PycharmProjects/parsing_html/Pliki zewnętrzne/scrapped/")
search_name = urllib.parse.quote_plus(url)
filename = os.path.join(scrapped_dir + search_name + ".txt")
r = urllib.request.urlopen(url)
array = {}
# deciding if file in folder


@app.route('/getfile', methods=['GET'])
def getfile():
    if os.path.exists(filename):
        with open(filename, encoding="utf-8") as f:
            text = f.read()
            print(url + "Webpage opened from file")
            array[url] = text

    else:
        soup = bs4.BeautifulSoup(r, 'html.parser')
        for script in soup(["script", "style"]):
            script.extract()

        # saving raw soup in temp file
        with open(filename, "w+", encoding="utf-8") as f:
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
            array[url] = text
            f.write(text)

    return jsonify(array)

# >>>>IF YES:

# file = request.files['file']
# # appending to array
# file_content = file.read()

# >>>>IF NOT USE BS4 METHOD FROM BS_TEST:
#     file_content = file.read()


# @app.route('/getfile', methods=['GET'])
# def getfile():
#     return jsonify({url: file_content})


if __name__ == '__main__':
    app.run(debug='True')
