import paho
import socket
import paho.mqtt.client as mqtt
import logging

_LOGGER = logging.getLogger(__name__)


class MQTTClient:
    """ The MQTTClient sends and receives data over MQTT using Mosquitto. """

    def __init__(self, host, port):
        """
        Initializes the mqtt client. Overwrites the methods used by mqtt's own
        Client class and then connects to the broker.
        :param host: the hostaddress of the broker
        :param port: the mqtt port
        """
        self.host = host
        self.port = port
        self.client = mqtt.Client()
        self.subscribe_client = mqtt.Client()
        _LOGGER.debug("[SERVICES][MQTTCLIENT] init")
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.client.on_connect = self.on_connect
        self.subscribe_client.on_subscribe = self.on_subscribe
        self.is_connected = self.connect(host, port)

    def subscribe(self, topic):
        """
        Subscribes to a topic.
        :param topic: The address of the topic.
        :return: Returns true if the operation was successful. Returns false
        if not.
        """
        _LOGGER.debug("[SERVICES][MQTTCLIENT] Subscribe")
        try:
            subscribed = self.subscribe_client.subscribe(topic)[0]
            return True
        except socket.gaierror:
            _LOGGER.error("Could not connect to host: " + self.host +
                          " on port " + str(self.port))
            return False

        _LOGGER.debug("%s" % subscribed)

    def publish_message(self, topic, payload):
        """
        Publishes a message to a topic.
        :param topic: the address of the topic.
        :param payload: The data regarding the state of the topic.
        :return: Returns true if the operation was successful. Returns false
        if not.
        """
        _LOGGER.debug("[SERVICES][MQTTCLIENT] publish message")
        try:
            self.client.publish(topic, payload)
            return True
        except socket.gaierror:
            _LOGGER.error("Could not connect to host: " + self.host +
                          " on port " + str(self.port))
            return False

    def connect(self, host, port):
        """
        Connects to the mqtt broker.
        :return: Returns whether the client was able to connect or not.
        :return: Returns true if the operation was successful. Returns false
        if not.
        """
        _LOGGER.debug("[SERVICES][MQTTCLIENT] connect")
        try:
            self.client.connect(host, port)
            return True
        except socket.gaierror:
            _LOGGER.error("Could not connect to host: " + self.host +
                          " on port " + str(self.port))
        except ConnectionRefusedError as err:
            _LOGGER.error("Connection refused for host: " + self.host +
                          " on port " + str(self.port))
            return False

    def disconnect(self):
        """
        Disconnects from the mqtt broker.
        :return: Returns true if the operation was successful. Returns false
        if not.
        """
        _LOGGER.debug("[SERVICES][MQTTCLIENT] Disconnect")
        try:
            self.client.disconnect()
            return True
        except socket.gaierror:
            _LOGGER.error("Could not connect to host: " + self.host +
                          " on port " + str(self.port))
            return False

    def on_connect(self, client, userdata, flags, rc):
        """ Triggers when the client connects to a broker. """
        _LOGGER.debug("[SERVICES][MQTTCLIENT] Connected")

    def on_publish(self, client, userdata, mid):
        """
        Triggers when a message sent by
        the client has reached the broker (Successfully published).
        """
        _LOGGER.debug("[SERVICES][MQTTCLIENT] on_publish %", self.host)

    def on_subscribe(self, client, userdata, mid, granted_qos):
        """
        Triggers when the connected broker responds to a subscribe request
        from the client.
        """
        _LOGGER.debug('[SERVICES][MQTTCLIENT] on_subscribe %', self.host)

    def on_message(self, client, userdata, msg):
        """
        Triggers when one of the topics that the client has subscribed to
        receives a message.
        """
        _LOGGER.debug('[SERVICES][MQTTCLIENT] on_message %', self.host)
        _LOGGER.debug("Host: " + self.host + "Topic: ",
                      msg.topic + '\nMessage: ' + str(msg.payload))
