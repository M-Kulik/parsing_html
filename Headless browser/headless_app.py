import bs4
import urllib.request, urllib.error
from flask import Flask

app = Flask(__name__)


@app.route('/<path:url>', methods=['GET'])
def getfile(url):

    content = urllib.request.urlopen(url)
    soup = bs4.BeautifulSoup(content, 'lxml')
    # for script in soup(["script", "style"]):
    #     script.extract()

    # getting all <p> tags
    tags = []
    for tag in soup.find_all('p', class_=False):
        tags.append(tag)

    # getting all <p> tags parents
    ptags = []
    for ptag in tags:
        if ptag.parent is not None:
            if ptag.parent not in ptags:
                ptags.append(ptag.parent)

    for tagt in ptags:
        return tagt.text


if __name__ == '__main__':
    app.run(debug=True)


# TODO:
#   PROBLEMS
#   1. There is no spectfic class/id for all text sections,
#   2. Text sections ar not on the same tree level,
#   3. Text section tends to be in the same tag as side bars,
#   4. DOM elements have no one size format,
#   5. Text sections tends to be in biger DOM elements - can't chose section by size
#   6. bs4 finds all p tags, separated parents
#   7. Can't search for parent with most <p> tags, different parent tag division
#   TRY
#   1. Finding body by css size:
#        -by padding
#        -by px, %, vh;vw
#
#   getting all <p> tags and returning thier parents worked

#
# # works with first child
# a = max(tags, key=len).text
# print(a)
# exit()
# tags2 = []
#
#
# print(tags2)
# test = []
# for tagg in tags:
#     test.append(list([line for line in tagg.strings]))
# hi = max(test, key=len)
# print(test)
#
# hihi = max(hi, key=len)
#
    # SELENIUM WEBDRIVER
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('disable-gpu')
    # driver = webdriver.Chrome(options=options)
    # driver.get(adress)
    # content = driver.page_source
