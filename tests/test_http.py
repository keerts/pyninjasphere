# created by sharon
# Project team: TechMasters
import requests

import unittest
import httpretty

from pyninjasphere.services.HTTP.http_client import HTTPClient


class HTTPClientTest(unittest.TestCase):
    """
    Test class for retrieving data through http
    """
    @httpretty.activate
    def test_http_request(self):
        httpretty.register_uri(httpretty.GET, "http://mylink.com/", body="testdata")
        self.assertEquals(HTTPClient().get_data_with_http_request("http://mylink.com/"), "testdata")



