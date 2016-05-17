# created by simon
# Project team: TechMasters

import unittest

from pyninjasphere.logic.thing import Thing
from pyninjasphere.logic.device import Device


class ThingTestCase(unittest.TestCase):
    """
    Test class for Thing class
    """
    
    def setUp(self):
        self.dictionary = {"id": "1","type": "light", "name": "Spot 1", "device": None,
                "deviceId": "a137c933-cb48-4eff-80c8-ea81e279e377", "location": "test_location", "promoted": "true"}
        self.thing = Thing(**self.dictionary)
        self.device_mapping = {"id" : 1, "naturalId" : "test", "name" : "test", "thingId" : 2, "channels" : None, "signatures" : None}
        self.dictionary_with_device = {"id": "1","type": "light", "name": "Spot 1", "device": self.device_mapping,
                "deviceId": "a137c933-cb48-4eff-80c8-ea81e279e377", "location": "test_location", "promoted": "true"}
        self.thing_with_device = Thing(**self.dictionary_with_device)

    def tearDown(self):
        self.thing = None

    def test_name(self):
        self.assertEqual(self.thing.name, self.dictionary["name"])

    def test_location(self):
        self.assertEqual(self.thing.location, self.dictionary["location"])

    def test_id(self):
        self.assertEqual(self.thing.id, self.dictionary["id"])
        
    def test_type(self):
        self.assertEqual(self.thing.type, self.dictionary["type"])
        
    def test_device_none(self):
        self.assertEqual(self.thing.device, self.dictionary["device"])

    def test_device(self):
        self.assertEqual(self.thing_with_device.device.__dict__, Device(**self.device_mapping).__dict__)
        
    def test_deviceId(self):
        self.assertEqual(self.thing.deviceId, self.dictionary["deviceId"])
        
    def test_promoted(self):
        self.assertEqual(self.thing.promoted, self.dictionary["promoted"])
