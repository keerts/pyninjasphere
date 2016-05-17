# created by Simon
# Project team: TechMasters

import unittest
from pyninjasphere.logic.channel import Channel


class ChannelTestCase(unittest.TestCase):
    """
    Test class for Channel class
    """

    def setUp(self):
        self.arguments = {"topic": "testtopic", "schema": "testschema", "supportedMethods": "testmethod",
                          "supportedEvents": "testevent", "id": "testid", "protocol": "testprotocol", "deviceId": 4,
                          "lastState": {"timestamp": "2014-10-18 21:31:12", "payload": "teststate"}}
        self.channel = Channel(**self.arguments)

    def tearDown(self):
        self.channel = None

    def test_topic(self):
        self.assertEqual(self.channel.topic, self.arguments["topic"])

    def test_schema(self):
        self.assertEqual(self.channel.schema, self.arguments["schema"])

    def test_supportedMethods(self):
        self.assertEqual(self.channel.supportedMethods, self.arguments["supportedMethods"])

    def test_supportedEvents(self):
        self.assertEqual(self.channel.supportedEvents, self.arguments["supportedEvents"])

    def test_id(self):
        self.assertEqual(self.channel.id, self.arguments["id"])

    def test_protocol(self):
        self.assertEqual(self.channel.protocol, self.arguments["protocol"])

    def test_deviceId(self):
        self.assertEqual(self.channel.deviceId, self.arguments["deviceId"])

    def test_lastState_timestamp(self):
        self.assertEqual(self.channel.lastState.timestamp, self.arguments["lastState"]["timestamp"])

    def test_lastState_payload(self):
        self.assertEqual(self.channel.lastState.payload, self.arguments["lastState"]["payload"])
