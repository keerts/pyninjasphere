#created by: Wilko
#Project team: TechMasters

import paho.mqtt.client as mqtt
import threading

class MQTTClient:
    'The MQTTClient sends and receives data over MQTT using Mosquitto'

    def __init__(self, host, port):
        self.client = mqtt.Client()
        self.subscribe_client = mqtt.Client()
        print("[SERVICES][MQTTCLIENT] init")
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.client.on_connect = self.on_connect
        self.subscribe_client.on_subscribe = self.on_subscribe
        self.connect(host, port)

    def subscribe(self,topic):
        print("[SERVICES][MQTTCLIENT] subscribe")
        print("%s" % self.subscribe_client.subscribe(topic)[0])


    def publishMessage(self, topic, payload):
        print("[SERVICES][MQTTCLIENT] publish message")
        self.client.publish(topic, payload)

    def connect(self, host, port):
        print("[SERVICES][MQTTCLIENT] connect")
        self.client.connect(host, port)
        self.subscribe_client.connect(host,port)

    def disconnect(self):
        print("[SERVICES][MQTTCLIENT] disconnect")
        self.client.disconnect()

    def on_connect(self, client, userdata, flags, rc):
        print("[SERVICES][MQTTCLIENT] on_connect")
        self.client.subscribe("test/topic")

    def on_publish(self, client, userdata, mid):
        print("[SERVICES][MQTTCLIENT] on_publish")

    def on_subscribe(self, client, userdata, mid, granted_qos):
        print("[SERVICES][MQTTCLIENT] on_subscribe")

    def on_message(self, client, userdata, msg):
        print("[SERVICES][MQTTCLIENT] on_message")
        print("Topic: ", msg.topic+'\nMessage: '+str(msg.payload))



