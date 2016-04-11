"""
The Ninjasphere 'things' api
"""
import urllib.request
import json
import codecs


class Node:
    """
    Represents the thing type 'node'
    """

    PORT = 8000
    PATH = '/rest/v1/things'

    def __init__(self, host):
        self.host = host

    def _construct_url(self):
        """
        Creates the full url to the node
        """
        return 'http://' + self.host + ':' + repr(self.PORT) + self.PATH

    def get_all_things(self):
        """
        Gets all the things
        """
        response = urllib.request.urlopen(self._construct_url())
        if response.code == 200:
            reader = codecs.getreader("utf-8")
            payload = json.load(reader(response))
            return payload

    def get_things(self, thing_type):
        """
        Gets all the things of type 'type'
        """
        return self.get_all_things
