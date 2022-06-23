import re
import cloudscraper

from message import ResponseInfo


class Agent:
    def __init__(self):
        self.scraper = cloudscraper.create_scraper()

    def get_url_set(self, request_info_list=[], *args):
        responses_list = []
        for req_info in request_info_list:
            # try:
            if (req_info.method == "GET"):
                resp = self.scraper.get(url=req_info.url)
                responses_list.append(ResponseInfo(req_info.id, resp.text))
            if (req_info.method == "POST"):
                resp = self.scraper.post(
                    url=req_info.url, data=req_info.data)
                responses_list.append(ResponseInfo(req_info.id, resp.text))
        # except:
        #     responses_list.append(ResponseInfo(
        #         req_info.id, "Something went wrong."))

        return responses_list
