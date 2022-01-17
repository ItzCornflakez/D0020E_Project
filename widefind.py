from threading import Thread
from transform import Transform, Vector3
import paho.mqtt.client as mqtt
import json


class WideFind(Thread):

    def __init__(self, url: str, port: int):
        Thread.__init__(self)

        # MQTT IP for WideFind
        self.broker_url = url
        self.broker_port = port

        # MQTT Client set up
        self.__client = mqtt.Client()
        self.__client.on_connect = self.__on_connect
        self.__client.on_message = self.__on_message

        # WideFind variables
        self.debug = False

    def run(self, debug=False) -> None:
        self.__client.connect(self.broker_url, self.broker_port)
        self.__client.loop_start()
        self.debug = debug

        self.__client.subscribe("#")  # '#' means subscribe to all topics

    def __on_connect(self, client, userdata, flags, rc, properties=None):
        if self.debug:
            print("Connected to " + self.broker_url + ":" + self.broker_port + " with reason code: " + rc)
            # TODO: Remove 'reason code' rc if it is useless

    def __on_message(self, client, userdata, message):
        mqtt_message_str = message.payload.decode()
        mqtt_message_json = json.loads(mqtt_message_str)
        mqtt_message_list = mqtt_message_json["message"].split(',')

        # TODO: Clean up unnecessary code, added for now to skip look up
        position = Vector3()
        position.x = mqtt_message_list[2]
        position.y = mqtt_message_list[3]
        position.z = mqtt_message_list[4]

        tracker_id = mqtt_message_list[0][7:]

        # TODO: Decide if tracker_id is unique. If it is add it to list of trackers else update already existing one
        # TODO: Add observer design pattern so that anyone can subscribe to WideFind events
        # TODO: Add documentation to public functions and class
        # https://refactoring.guru/design-patterns/observer/python/example

        # The rest of the code provided is probably for camera look at coordinates!


class Tracker:

    def __init__(self, tracker_id: str):
        self.tracker_id = tracker_id
        self.transform = Transform()
