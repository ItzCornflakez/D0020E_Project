from abc import abstractmethod, ABC
from enum import Enum
import numpy
import requests


class Camera:

    @abstractmethod
    def rotate(self, yaw, pitch):
        """Rotate camera relative to current orientation.

        Args:
            yaw (int): "Horizontal" rotation
            pitch (int): "Vertical" rotation
        """

        pass


class HDIntegratedCamera(Camera):
    # Values for converting between camera hex and degrees
    class Conversion:
        DEG_TO_HEX_YAW = 42480 / 350
        DEG_TO_HEX_PITCH = 14562 / 120

    class Commands:
        ROTATE = "APC"

    class Status:
        OK = 200

    def __init__(self, baseurl: str, position: numpy.array, zero: numpy.array):
        # Communication variables
        self.__BASEURL = baseurl

        # Orientation variables
        self.__position = position
        self.__orientation = numpy.array([0, 0, 0])
        self.__unit_vector_zero = numpy.subtract(zero, position) / numpy.linalg.norm(numpy.subtract(zero, position))

        # Reset camera rotation
        self.look_at_coordinate(zero)

    @staticmethod
    def convert_degrees(degrees: int, conv: float) -> str:
        """Converts degrees to hexadecimal for rotation command to HD Integrated Camera"""

        degrees *= conv
        degrees = int(degrees)
        degrees += (int("0x2d08", 16)-5)
        degrees = hex(degrees)
        return str(degrees)[2:].upper()

    def rotate(self, yaw: int, pitch: int):
        """Rotate camera relative to current orientation."""

        new_yaw = (yaw + self.__orientation[1])
        new_pitch = (pitch + self.__orientation[2])

        if new_yaw > 360 or new_pitch > 180:
            raise Exception("Rotation out of range")

        return self.absolute_rotate(new_yaw, new_pitch)

    def absolute_rotate(self, new_yaw: int, new_pitch: int):
        """Rotate camera relative to zero pointer"""
        url = self.__BASEURL + self.Commands.ROTATE                             # Rotate command
        url += self.convert_degrees(new_yaw, self.Conversion.DEG_TO_HEX_YAW)      # Yaw argument
        url += self.convert_degrees(new_pitch, self.Conversion.DEG_TO_HEX_PITCH)  # Pitch argument
        url += "&res=1"

        req = requests.get(url=url)

        if req.status_code != self.Status.OK:
            raise Exception("Communication with camera failed")

        self.__orientation[1] = new_yaw
        self.__orientation[2] = new_pitch

    def look_at_coordinate(self, coordinate: numpy.array):
        vector_coord = numpy.subtract(coordinate, self.__position)
        unit_vector_coord = vector_coord / numpy.linalg.norm(vector_coord)
        unit_vector_zero = self.__unit_vector_zero

        dot_product = numpy.dot(unit_vector_coord, unit_vector_zero)
        rad_angle = numpy.arccos(dot_product)
        deg_angle = int(rad_angle * 180 / 3.1415)
        print(rad_angle)
        print(deg_angle)
        self.absolute_rotate(deg_angle, 150)
