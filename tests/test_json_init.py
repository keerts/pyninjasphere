import unittest
from pyninjasphere.services.codec import Codec


class JsonTestCase(unittest.TestCase):
    """ Test class for the complete service class. """

    def disabled_test_gerstree(self):
        """ Test the json that is returned by gerstree's sphere"""
        data = open('tests/sample_data.json', 'r').read()
        things = Codec.decode_things(data)
        self.assertEqual(things, things)

    def test_vertikar(self):
        """ Test the json that is returned by vertikar's sphere"""
        data = open('tests/vertikar.json', 'r').read()
        things = Codec.decode_things(data)
        self.assertEqual(things, things)
