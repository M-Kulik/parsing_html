from flask import Flask
from flask import render_template
import bs4
import urllib
import urllib.request

app = Flask(__name__)


@app.route('/website')
def website():
    return render_template('wiki.html')


@app.route('/<path:url>', methods=['GET'])
def getfile(url):

    r = urllib.request.urlopen(url)
    soup = bs4.BeautifulSoup(r, 'lxml-xml')

    for script in soup(["script", "style"]):
        script.extract()

    # contents of body
    tags = []
    for kid in soup.body.contents:
        if kid.name is not None:
            tags.append(kid)

    # TODO: get children of max[tags],
    #  put them in separate lists in one list,
    #  then get the longest list,
    #  work on these tags

    a = max(tags, key=len).text
    return a
