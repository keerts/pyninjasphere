# created by sharon
# Project team: TechMasters

import unittest
from pyninjasphere.logic.thing import Thing


class ThingTestCase(unittest.TestCase):
    """
    Test class for Thing class
    """

    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(ThingTestCase('test_name'))
        suite.addTest(ThingTestCase('test_location'))
        return suite()

    def setUp(self):
        self.thing = Thing(1, "light", "Spot 1", "a137c933-cb48-4eff-80c8-ea81e279e377", "test_location", "true", "T_device")

    def tearDown(self):
        self.thing = None

    def test_name(self):
        self.assertEqual(self.thing.name, "Spot 1")

    def test_location(self):
        self.assertEqual(self.thing.location, "test_location")
