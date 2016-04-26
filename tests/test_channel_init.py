# created by sharon
# Project team: TechMasters

import unittest
from pyninjasphere.logic.channel import Channel


class ChannelTestCase(unittest.TestCase):
    """
    Test class for Channel class
    """

    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(ChannelTestCase('test_name'))
        suite.addTest(ChannelTestCase('test_location'))
        return suite()

    def setUp(self):
        self.channel = Channel("$device/b35628d81b/channel/brightness", "http://schema.ninjablocks.com/protocol/brightness",
                             ["set"], [], "brightness", "brightness", "b35628d81b", 1459951632758, 0.2627450980392157)

    def tearDown(self):
        self.thing = None

    def test_schema(self):
        self.assertEqual(self.channel.schema, "http://schema.ninjablocks.com/protocol/brightness")

    def test_protocol(self):
        self.assertEqual(self.channel.protocol, "brightness")
