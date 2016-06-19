import requests

import unittest
import httpretty
from logging import getLogger
from testfixtures import LogCapture
from pyninjasphere.services.HTTP.http_client import HTTPClient

logger = getLogger()


class HTTPClientTest(unittest.TestCase):
    """ Test class for retrieving data through http. """

    @httpretty.activate
    def test_http_request(self):
        httpretty.register_uri(
            httpretty.GET, "http://mylink.com/", body="testdata")
        self.assertEquals(HTTPClient().get_data_with_http_request(
            "http://mylink.com/"), "testdata")

    def test_http_request_exception(self):
        with LogCapture() as l:
            try:
                HTTPClient().request(" ")
            except:
                logger.error('error occurred', exc_info=True)
        l.check(('pyninjasphere.services.HTTP.http_client',
                 'ERROR', "Invalid url, "
                          "please insert a valid url."))

    def test_response(self):
        httpretty.register_uri(
            httpretty.GET, "http://mylink.com/", body="testdata")
        http_client = HTTPClient()
        request = http_client.request("http://mylink.com/")
        with LogCapture() as l:
            try:
                http_client.create_response(request)
            except:
                logger.error('error occurred', exc_info=True)

    def test_response_exception_empty_request(self):
        http_client = HTTPClient()
        request = None
        with LogCapture() as l:
            try:
                http_client.create_response(request)
            except:
                logger.error('error occurred', exc_info=True)
        l.check(('pyninjasphere.services.HTTP.http_client',
                 'ERROR', "Invalid request, "
                          "please insert a valid request."))

    def test_response_exception(self):
        http_client = HTTPClient()
        request = http_client.request("")
        with LogCapture() as l:
            try:
                http_client.create_response(request)
            except:
                logger.error('error occurred', exc_info=True)
        l.check(('pyninjasphere.services.HTTP.http_client',
                 'ERROR', "Invalid request, "
                          "please insert a valid request."))
