import json
import requests
from bs4 import BeautifulSoup
from open_graph_nodes import OpenGraphNode

url = 'https://www.imdb.com/title/tt0117500/'


def scrape(url):

    data = {"yo": 6}

    jdata = json.dumps(data)

    headers = {'Content-Type': "application/json; charset=xxxe", 'Accept': "application/json"}

    params = {"url": "https://www.imdb.com/title/tt0117500/"}

    response = requests.get(url=url, params=params, json=jdata, headers=headers)

    # print(response.status_code)
    # print(response.raise_for_status())
    # print(response.status_code)
    # print(response.cookies)
    # print(response.headers)

    # print(response.content)

    html = response.content

    soup = BeautifulSoup(html, "html.parser")

    # print(parsed_html.prettify())
    # print(parsed_html)


    for tag in soup.find_all("meta"):

        p = tag.get("property", None)
        c = tag.get("content", None)

        if p is not None:

            if 'og:' in p:
                print(f"property:  {p}      content:  {c} " )

    print()
    print()

    _title = soup.find("meta",  property="og:title")
    _url = soup.find("meta",  property="og:url")
    _type = soup.find("meta",  property="og:type")
    _image = soup.find("meta",  property="og:image")

    print(_title["content"] if _title else "No meta title given")
    print(_url["content"] if _url else "No meta url given")
    print(_url["content"] if _image else "No meta image given")


    if _url:
        _url = _url["content"]

    if _title:
        _title = _title["content"]

    if _type:
        _type = _type["content"]


    node = OpenGraphNode(url=_url, type=_type, title=_title)

    return node



if __name__ == '__main__':

    scrape(url)