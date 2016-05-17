#created by: Wilko
#Project team: TechMasters

import urllib.request


class HTTPClient:
    """The HTTPClient sends and receives data over HTTP"""

    def __init__(self, headers = None):
        self.values = None
        self.headers = headers
        if headers is None:
            self.headers = {
                'Content-Type': 'application/json',
            }

    def get_data_with_http_request(self, url):
        """
        Gets data from an url
        :param url: http url
        :return: the requested data
        """
        print("[SERVICES][HTTPCLIENT] sendHTTPRequest")
        request = self.create_request(url)
        response = self.create_response(request)
        data = self.decode_response(response)
        return data

    def create_request(self, url):
        """
        Creates a request object
        :param url: http url
        :return: A request object
        """
        return urllib.request.Request(url)

    @staticmethod
    def create_response(request):
        """
        Creates a response object containing the data gotten from the url
        :param request: A request object
        :return: A response object
        """
        return urllib.request.urlopen(request)

    @staticmethod
    def decode_response(response):
        """
        Reads the data from a response object and returns it
        :param response: A response object
        :return: Fetched data
        """
        return response.read().decode('utf-8')