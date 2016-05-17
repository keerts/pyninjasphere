#created by: Wilko
#Project team: TechMasters

from pyninjasphere.services.HTTP.http_client import HTTPClient
from pyninjasphere.logic.node import Node
from pyninjasphere.services.codec import Codec
from pyninjasphere.services.MQTT.mqtt_client import MQTTClient

class Service:
    """Handles all data flows between HA and the Ninja Sphere"""

    def __init__(self, host, mqtt_port = 1883, rest_port = 8000):
        self.http_client = HTTPClient()
        self.rest_port = rest_port
        self.node = Node()
        self.codec = Codec()
        self.host = host
        self.mqtt_port = mqtt_port

    def get_data_with_http(self, url):
        """
        Gets data from a http url
        :param url: http url
        :return:
        """
        return self.http_client.get_data_with_http_request(url)

    def get_all_things(self):
        """
            Gets the things in json format over http then decodes them and stores them inside node's thing attribute
            :return: decoded things
        """

        url = "http://" + self.host + ":" + self.rest_port +"/rest/v1/things"
        print (url)
        data = self.get_data_with_http(url)
        things = Codec.decode_things(data)
        self.node.things = things
        return self.node.things

    def publish_message_with_mqtt(self, topic, payload):
        """
        Publishes a payload to a mqtt-topic
        :param topic: the address of the topic
        :param payload: the content of the message being sent
        """
        self.mqtt_client.publish_message(topic, payload)



