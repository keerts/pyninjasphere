import logging
from pyninjasphere.services.HTTP.http_client import HTTPClient
from pyninjasphere.logic.node import Node
from pyninjasphere.services.codec import Codec
from pyninjasphere.services.MQTT.mqtt_client import MQTTClient

_LOGGER = logging.getLogger(__name__)


class Service:
    """ Handles all data flows between HA and the Ninja Sphere. """

    def __init__(self, host, mqtt_port=1883, rest_port=8000, debug=False):
        self.debug = debug
        if debug:
            headers = {
                'Content-Type': 'application/json',
                'JsonStub-User-Key': 'e2ace556-284c-4b21-9dc5-9900cf4d7236',
                'JsonStub-Project-Key': '7b32ef13-8be8-4e6d-8924-fcc33efb476b'
            }
            self.http_client = HTTPClient(headers=headers)
        else:
            self.http_client = HTTPClient()

        self.rest_port = rest_port
        self.node = Node()
        self.codec = Codec()
        self.host = host
        self.mqtt_port = mqtt_port
        self.mqtt_client = MQTTClient(host, mqtt_port)

    def get_data_with_http(self, url):
        """
        Gets data from a http url
        :param url: http url
        :return: Returns true if the operation was successful. Returns false
        if not.
        """
        return self.http_client.get_data_with_http_request(url)

    def get_all_things(self):
        """
            Gets the things in json format over http
            then decodes them and stores them inside node's thing attribute.
            :return: Decoded things or an empty list if none were found.
        """
        url = "http://" + str(self.host) + ":" + \
            str(self.rest_port) + "/rest/v1/things"
        if self.debug:
            url = 'http://jsonstub.com/exampledata'
            _LOGGER.debug(url)

        data = self.get_data_with_http(url)
        if data is not None:
            things = Codec.decode_things(data)
            self.node.things = things
            return self.node.things
        return []

    def publish(self, topic, payload):
        """
        Publishes a payload to a mqtt-topic.
        :param topic: The address of the topic.
        :param payload: The content of the message being sent.
        :return: Returns true if the operation was successful. Returns false
        if not.
        """
        return self.mqtt_client.publish_message(topic, payload)

    def subscribe(self, topic):
        """
        Subscribes the mqtt client to a topic.
        :param topic: Topic to subscribe to.
        :return: Returns true if the operation was successful. Returns false
        if not.
        """
        return self.mqtt_client.subscribe(topic)
