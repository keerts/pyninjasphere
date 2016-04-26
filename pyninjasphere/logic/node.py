"""
The Ninjasphere 'things' api
"""

import jsonmodels.models as jsonmodels

class Node(jsonmodels.Base):
    """
    Represents the thing type 'node'
    """

    PORT = 8000
    PATH = '/rest/v1/things'

    def __init__(self):
        self.things = None

    def _construct_url(self):
        pass
        """
        Creates the full url to the node
        """
        # return 'http://' + self.host + ':' + repr(self.PORT) + self.PATH

    def get_all_things(self):

        return self.things

    def get_things(self, thing_type):
        """
        Gets all the things of type 'type'
        """
        return self.get_all_things
