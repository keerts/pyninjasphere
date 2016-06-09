import unittest
from pyninjasphere.logic.device import Device
from pyninjasphere.logic.device import Channel


class DeviceTestCase(unittest.TestCase):
    """ Test class for Device class. """

    def setUp(self):
        self.arguments = {"id": 1, "naturalId": "test", "name": "test",
                          "thingId": 2, "channels": None,
                          "signatures": {"test"}}
        self.device = Device(**self.arguments)
        channel_mapping = {"topic": "testtopic", "schema": "testschema",
                           "supportedMethods": "testmethod",
                           "supportedEvents": "testevent", "id":
                               "testid", "protocol": "testprotocol",
                           "deviceId": 4, "lastState": None}
        self.mapping_of_channel_mappings = [channel_mapping, channel_mapping]
        self.arguments_with_channels = {"id": 1, "naturalId": "test",
                                        "name": "test", "thingId": 2,
                                        "channels":
                                            self.mapping_of_channel_mappings,
                                        "signatures": {"test"}}
        self.device_with_channels = Device(**self.arguments_with_channels)

    def tearDown(self):
        self.device = None

    def test_id(self):
        self.assertEqual(self.device.id, self.arguments["id"])

    def test_naturalId(self):
        self.assertEqual(self.device.naturalId, self.arguments["naturalId"])

    def test_name(self):
        self.assertEqual(self.device.name, self.arguments["name"])

    def test_thingId(self):
        self.assertEqual(self.device.thingId, self.arguments["thingId"])

    def test_channels_none(self):
        self.assertEqual(self.arguments["channels"], self.device.channels)

    def test_channels(self):
        x = 0
        for channel_mapping in self.mapping_of_channel_mappings:
            self.assertEqual(Channel(**channel_mapping).__dict__,
                             self.device_with_channels.channels[x].__dict__)
            x += 1

    def test_signatures(self):
        self.assertEqual(self.device.signatures, self.arguments["signatures"])
