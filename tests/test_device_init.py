# created by sharon
# Project team: TechMasters

import unittest
from pyninjasphere.logic.device import Device


class DeviceTestCase(unittest.TestCase):
    """
    Test class for Device class
    """

    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(DeviceTestCase('test_name'))
        suite.addTest(DeviceTestCase('test_location'))
        return suite()

    def setUp(self):
        self.device = Device("$device/b35628d81b", "http://schema.ninjablocks.com/service/device", "setBatch", [],
                              "b35628d81b", "8", "Spot 1", "a137c933-cb48-4eff-80c8-ea81e279e377", "signature", [])


    def tearDown(self):
        self.thing = None

    def test_schema(self):
        self.assertEqual(self.channel.schema, "http://schema.ninjablocks.com/protocol/brightness")

    def test_protocol(self):
        self.assertEqual(self.channel.protocol, "brightness")

