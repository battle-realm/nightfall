from urllib import response
from flask import Flask, request
import os
from types import SimpleNamespace
import json
import jsonpickle

from agent import *
from message import RequestInfo

app = Flask(__name__)


@app.route('/', methods=['POST'])
def get_urls():
    pre_request_info_list = json.loads(request.get_data())
    request_info_list = []
    for req_info in pre_request_info_list:
        request_info_list.append(RequestInfo(
            req_info.get("id"), req_info.get("method"), req_info.get("url"), req_info.get("post_data")))

    scraper = Agent()
    response_info_list = scraper.get_url_set(request_info_list)
    return jsonpickle.encode(response_info_list, make_refs=False, unpicklable=False)


if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=5000)
