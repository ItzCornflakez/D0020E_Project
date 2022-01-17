from transform import Vector3
import paho.mqtt.client as mqtt
import json


class WideFind:
    """Used for connecting to a WideFind sensor."""

    def __init__(self, url: str, port: int):
        # MQTT IP for WideFind
        self.broker_url = url
        self.broker_port = port

        # MQTT Client set up
        self.__client = mqtt.Client()
        self.__client.on_connect = self.__on_connect
        self.__client.on_message = self.__on_message

        # WideFind variables
        self.trackers = {}
        self.debug = False

    def run(self, debug=False) -> None:
        self.__client.connect(self.broker_url, self.broker_port)
        self.__client.loop_start()
        self.debug = debug

        self.__client.subscribe("#")  # '#' means subscribe to all topics

    def __on_connect(self, client, userdata, flags, rc, properties=None):
        if self.debug:
            print("Connected to " + self.broker_url + ":" + self.broker_port)

    def __on_message(self, client, userdata, message):
        # Decode message and put into list
        mqtt_message_str = message.payload.decode()
        mqtt_message_json = json.loads(mqtt_message_str)
        mqtt_message_list = mqtt_message_json["message"].split(',')

        # Update tracker information
        tracker_id = mqtt_message_list[0][7:]
        position = Vector3()
        position.x = mqtt_message_list[2]
        position.y = mqtt_message_list[3]
        position.z = mqtt_message_list[4]

        self.trackers[tracker_id] = position

        if self.debug:
            print("Tracker with id: " + tracker_id + ", currently positioned at " + position)

        # TODO: Test if threading is really necessary...
        # TODO: Add observer design pattern so that anyone can subscribe to WideFind events
        # https://refactoring.guru/design-patterns/observer/python/example

        # The rest of the code provided is probably for camera look at coordinates!
