from abc import abstractmethod, ABC
from enum import Enum
from transform import Transform, Vector3
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

    def __init__(self, baseurl: str):
        # Orientation variables
        self.__transform = Transform()

        # Communication variables
        self.__BASEURL = baseurl

    @staticmethod
    def convertDegrees(degrees: int, conv: float) -> str:
        """Converts degrees to hexadecimal for rotation command to HD Integrated Camera"""

        degrees *= conv
        degrees = int(degrees)
        degrees += (int("0x2d08", 16)-5)
        degrees = hex(degrees)
        return str(degrees)[2:].upper()

    def rotate(self, yaw: int, pitch: int):
        """Rotate camera relative to current orientation."""

        newYaw = (yaw + self.__transform.eulerAngle.y)
        newPitch = (pitch + self.__transform.eulerAngle.z)

        if newYaw > 360 or newPitch > 90:
            raise Exception("Rotation out of range")

        return self.absoluteRotate(newYaw, newPitch)

    def absoluteRotate(self, newYaw: int, newPitch: int):
        """Rotate camera relative to zero pointer"""

        url = self.__BASEURL + self.Commands.ROTATE                             # Rotate command
        url += self.convertDegrees(newYaw, self.Conversion.DEG_TO_HEX_YAW)      # Yaw argument
        url += self.convertDegrees(newPitch, self.Conversion.DEG_TO_HEX_PITCH)  # Pitch argument
        url += "&res=1"

        req = requests.get(url=url)

        if req.status_code != self.Status.OK:
            raise Exception("Communication with camera failed")

        self.__transform.eulerAngle.y = newYaw
        self.__transform.eulerAngle.z = newPitch
