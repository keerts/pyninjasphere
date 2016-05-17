# created by: Wilko
# Project team: TechMasters

import paho.mqtt.client as mqtt
import threading


class MQTTClient:
    """The MQTTClient sends and receives data over MQTT using Mosquitto"""

    def __init__(self, host, port):
        """
        Initializes the mqtt client.
        Overwrites the methods used by mqtt's own Client class and then connects to the broker.
        :param host: the hostaddress of the broker
        :param port: the mqtt port
        """
        self.host = host
        self.port = port
        self.client = mqtt.Client()
        self.subscribe_client = mqtt.Client()
        print("[SERVICES][MQTTCLIENT] init")
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.client.on_connect = self.on_connect
        self.subscribe_client.on_subscribe = self.on_subscribe
        self.connect(host, port)

    def subscribe(self, topic):
        """
        Subscribes to a topic
        :param topic: the address of the topic
        """
        print("[SERVICES][MQTTCLIENT] subscribe")
        print("%s" % self.subscribe_client.subscribe(topic)[0])

    def publish_message(self, topic, payload):
        """
        Publishes a message to a topic
        :param topic: the address of the topic
        :param payload: the data regarding the state of the topic
        """
        print("[SERVICES][MQTTCLIENT] publish message")
        self.client.publish(topic, payload)

    def connect(self, host, port):
        """
        Connects to the mqtt broker
        """
        print("[SERVICES][MQTTCLIENT] connect")
        self.client.connect(host, port)
        self.subscribe_client.connect(host, port)

    def disconnect(self):
        """
        Disconnects from the mqtt broker
        """
        print("[SERVICES][MQTTCLIENT] disconnect")
        self.client.disconnect()

    def on_connect(self, client, userdata, flags, rc):
        """
        Triggers when the client connects to a broker
        """
        print("[SERVICES][MQTTCLIENT] on_connect")
        self.client.subscribe("test/topic")

    def on_publish(self, client, userdata, mid):
        """
        Triggers when a message sent by the client has reached the broker (Successfully published)
        """
        print("[SERVICES][MQTTCLIENT] on_publish %", self.host)

    def on_subscribe(self, client, userdata, mid, granted_qos):
        """
        Triggers when the connected broker responds to a subscribe request from the client
        """
        print('[SERVICES][MQTTCLIENT] on_subscribe %', self.host)

    def on_message(self, client, userdata, msg):
        """
        Triggers when one of the topics that the client has subscribed to receives a message.
        """
        print('[SERVICES][MQTTCLIENT] on_message %', self.host)
        print("Topic: ", msg.topic + '\nMessage: ' + str(msg.payload))
