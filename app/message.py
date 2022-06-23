class RequestInfo:
    def __init__(self, id, method, url, post_data):
        self.id = id
        self.method = method
        self.url = url
        self.data = post_data


class ResponseInfo:
    def __init__(self, id, response):
        self.id = id
        self.response = response
