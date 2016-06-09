import urllib.request
import logging

_LOGGER = logging.getLogger(__name__)


class HTTPClient:
    """ The HTTPClient sends and receives data over HTTP. """

    def __init__(self, headers={}):
        self.values = None
        self.headers = headers
        if headers == {}:
            self.headers = {
                'Content-Type': 'application/json',
            }

    def get_data_with_http_request(self, url):
        """
        Gets data from an url.
        :param url: http url
        :return: the requested data
        """
        _LOGGER.debug("[SERVICES][HTTPCLIENT] sendHTTPRequest")
        try:
            request = self.request(url)
            response = self.create_response(request)
            data = self.decode_response(response)
        except TypeError:
            _LOGGER.error("Could not fetch data from "+url)
            return None
        return data

    def request(self, url):
        """
        Creates a request object.
        :param url: http url
        :return: A request object
        """
        requested_data = None
        try:
            requested_data = urllib.request.Request(url, headers=self.headers)
        except urllib.error.URLError as err:
            _LOGGER.error("Could not connect: " + err.reason)
        except urllib.error.HTTPError as err:
            _LOGGER.error("Server return code " + err.code + ". " +
                          err.reason + " Error caused by the following "
                                       "header(s): " + err.headers + ".")
        except urllib.error.ContentTooShortError as err:
            _LOGGER.error("Could not connect! The amount of the downloaded "
                          "data is less than the expected amount (given by "
                          "the Content-Length header).")
        except ValueError as err:
            _LOGGER.error("Invalid url, please insert a valid url.")
        return requested_data

    @staticmethod
    def create_response(request):
        """
        Creates a response object containing the data gotten from the url.
        :param request: A request object
        :return: A response object
        """
        opened_url = None
        try:
            opened_url = urllib.request.urlopen(request)
        except urllib.error.URLError as err:
            _LOGGER.error("Could not connect: " + err.reason)
        except urllib.error.HTTPError as err:
            _LOGGER.error("Server return code " + err.code + ". " +
                          err.reason + " Error caused by the following "
                                       "header(s): " + err.headers + ".")
        except urllib.error.ContentTooShortError as err:
            _LOGGER.error("Could not connect! The amount of the downloaded "
                          "data is less than the expected amount (given by "
                          "the Content-Length header).")
        except AssertionError as err:
            _LOGGER.error("Invalid request, please insert a valid request.")
        except AttributeError as err:
            _LOGGER.error("Invalid request, please insert a valid request.")

        return opened_url

    @staticmethod
    def decode_response(response):
        """
        Reads the data from a response object and returns it.
        :param response: A response object
        :return: Fetched data
        """
        return response.read().decode('utf-8')
