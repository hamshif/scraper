import json
from flask import Flask, request
from scrape import scrape
# from open_graph_node import OpenGraphNode, db

app = Flask(__name__)


@app.route('/stories', methods=['GET', 'POST', 'DELETE', 'PUT'])
def post_stories():

    # print(f'args:\n{request.args}\n\n')
    # print(f'data:\n{request.data}\n\n')
    # print(f'headers:\n{request.headers}\n\n')
    # print(f'mimetypes:\n{request.accept_mimetypes}\n\n')
    # print(f'encodings:\n{request.accept_encodings}\n\n')


    print("request method: " + request.method)

    if request.method != 'POST':

        return 'Hello there scraper please use POST!'

    else:

        url = request.args.get('url')

        print(f'did you ask for scraping of:  {url}    ?\n')

        data = {"please add url to params": 7}

        if url is None:

            return json.dumps(data)


        node = scrape(url)

        print(f"node.url: {node.url}")

        print(node)

        print('gamgee')
        data = node.as_dict()

        return json.dumps(data)


@app.route('/stories/<canonical_url_id>')
def get_stories(canonical_url_id):


    return f'Hello there {canonical_url_id} scraper!'


@app.route('/<name>')
def hello_name(name):
    return f"Hello {name} world!"



if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')

