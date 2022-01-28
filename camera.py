import numpy
import requests


class HDIntegratedCamera:
    class Conversion:
        """Contains values for translating degrees to camera's hex values."""
        DEG_TO_HEX_YAW = 42480 / 350
        DEG_TO_HEX_PITCH = 14562 / 120

    class Commands:
        """Contains strings for different commands the camera accepts."""
        ROTATE = "APC"

    class Status:
        """Contains status values from camera."""
        OK = 200

    def __init__(self, baseurl: str):
        # Communication variables
        self.__BASEURL = baseurl

        # Orientation variables
        self.__current_yaw = 0
        self.__current_pitch = 0

    @staticmethod
    def convert_degrees(degrees: int, conv: float) -> str:
        """Converts degrees to hexadecimal for rotation command to HD Integrated Camera"""

        degrees *= conv
        degrees = int(degrees)
        degrees += (int("0x2d08", 16)-5)
        degrees = hex(degrees)
        return str(degrees)[2:].upper()

    def rotate(self, new_yaw: int, new_pitch: int):
        """Rotate camera relative to zero pointer"""
        url = self.__BASEURL + self.Commands.ROTATE                             # Rotate command
        url += self.convert_degrees(new_yaw, self.Conversion.DEG_TO_HEX_YAW)      # Yaw argument
        url += self.convert_degrees(new_pitch, self.Conversion.DEG_TO_HEX_PITCH)  # Pitch argument
        url += "&res=1"

        req = requests.get(url=url)

        if req.status_code != self.Status.OK:
            raise Exception("Communication with camera failed")

        self.__current_yaw = new_yaw
        self.__current_pitch = new_pitch
