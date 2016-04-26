#created by: Wilko
#Project team: TechMasters

from pyninjasphere.services.HTTP.http_client import HTTPClient
from pyninjasphere.logic.node import Node
from pyninjasphere.services.codec import Codec
from pyninjasphere.services.MQTT.mqtt_client import MQTTClient

class Service:
    'Handles all data flows between HA and the Ninja Sphere'

    def __init__(self, host, mqtt_port = 8000, htpp_port = 80):
        self.http_client = HTTPClient()
        self.mqtt_client = MQTTClient(host, mqtt_port)
        self.node = Node()
        self.codec = Codec()
        self.host = host
        self.mqtt_port = mqtt_port #NinjaSphere port = 8000

    def get_data_with_http(self, url):
        return self.http_client.get_data_with_http_request(url)

    def get_all_things(self):
        data = self.get_data_with_http("http://jsonstub.com/exampledata")
        things = self.codec.decode_things(data)
        self.node.things = things
        return self.node.things

    def publish_message_with_mqtt(self, topic, payload):
        self.mqtt_client.publishMessage(topic, payload)


# service = Service("")
# service.get_all_things()



