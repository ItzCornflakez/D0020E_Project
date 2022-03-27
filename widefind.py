from abc import ABC

import numpy as np
import paho.mqtt.client as mqtt
import json
from observer_pattern.observer import Subject, Observer


class WideFind(Subject, ABC):
    """
    Receives information regarding its trackers from physical WideFind sensor and notifies observers.

    Args:
        url (str): WideFind's URL that should be used.
        port (int): WideFind's port that should be used.
    """

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

        # Observer design pattern
        self._observers = []

    def run(self, subscription: str = "#", debug: bool = False) -> None:
        """
        When executed start receiving tracker data regarding subscription.

        Args:
            subscription (str): What events should WideFind tell us about, default is everything.
            debug (bool): Should the program print details regarding the information it receives?
        """
        self.__client.connect(self.broker_url, self.broker_port)
        self.__client.loop_start()
        self.debug = debug

        self.__client.subscribe(subscription)

    def __on_connect(self, client, userdata, flags, rc, properties=None):
        if self.debug:
            print("WideFind: Connected to " + self.broker_url + ":" + str(self.broker_port))

    def __on_message(self, client, userdata, message):
        # Decode message and put into list
        mqtt_message_json = json.loads(message.payload)
        mqtt_message_list = mqtt_message_json["message"].split(',')

        # Update tracker information
        tracker_id = mqtt_message_list[0][7:]
        tracker_pos = np.array([int(mqtt_message_list[2]), int(mqtt_message_list[3]), int(mqtt_message_list[4])])

        self.trackers[tracker_id] = tracker_pos

        if self.debug:
            print("WideFind: Tracker with id: " + tracker_id + ", currently positioned at " + tracker_pos.__repr__())

        self.notify()

    # OBSERVER DESIGN PATTERN
    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

        if self.debug:
            print("WideFind: Attached an observer")

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

        if self.debug:
            print("WideFind: Detached an observer")

    def notify(self) -> None:
        if self.debug:
            print("WideFind: Notifying observers")

        for observer in self._observers:
            observer.update(self)


class Transform:
    """
        Transform of an object using WideFind coordinates. Contains functions for useful linear algebra calculations.

        Args:
            position (np.array): Position of object using WideFind's coordinate-system
            zero (np.array): some coordinate in front of object using WideFind's coordinate-system
            down (np.array): some coordinate underneath object using WideFind's coordinate-system
        """

    def __init__(self, position: np.array, zero: np.array, down: np.array):
        # Translate coordinates into zero and down vectors relative to position.
        zero_vec = np.subtract(zero, position)
        down_vec = np.subtract(down, position)

        # Create unit vectors for zero and down.
        self.zero_unit_vec = zero_vec / np.linalg.norm(zero_vec)
        self.down_unit_vec = down_vec / np.linalg.norm(down_vec)
        self.position = position

    def get_yaw_from_zero(self, coordinate: np.array) -> int:
        """
        Returns the angle between Transform's zero vector and coordinate given

        Args:
            coordinate (np.array): Coordinate to calculate relative angle to.
        """

        coord_vec = np.subtract(coordinate, self.position)
        coord_unit_vec = coord_vec / np.linalg.norm(coord_vec)

        # Calculate which side of the position the coordinate is at
        # Side > 0 -> first and second quadrant (0 - 180)
        # Side < 0 -> third and forth quadrant (180 - 360)
        # https://math.stackexchange.com/questions/214187/point-on-the-left-or-right-side-of-a-plane-in-3d-space
        matrix = np.array([self.down_unit_vec, self.zero_unit_vec, coord_unit_vec])
        side = np.linalg.det(matrix)

        # Calculate degrees for yaw
        dot_product = np.dot(coord_unit_vec, self.zero_unit_vec)
        rad_angle = np.arccos(dot_product)
        yaw_deg_angle = int(rad_angle * 180 / 3.1415)

        if side < 0:
            yaw_deg_angle = 360 - yaw_deg_angle

        return yaw_deg_angle

    def get_pitch_from_zero(self, coordinate: np.array) -> int:
        """
        Returns the angle between Transform's down vector and coordinate given

        Args:
            coordinate (np.array): Coordinate to calculate relative angle to.
        """

        coord_vec = np.subtract(coordinate, self.position)
        coord_unit_vec = coord_vec / np.linalg.norm(coord_vec)

        dot_product = np.dot(coord_unit_vec, self.down_unit_vec)
        rad_angle = np.arccos(dot_product)
        pitch_deg_angle = int(rad_angle * 180 / 3.1415)

        return pitch_deg_angle
