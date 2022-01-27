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

    def __init__(self, baseurl: str, position: numpy.array, zero: numpy.array, floor: numpy.array):
        # Communication variables
        self.__BASEURL = baseurl

        # TODO: Remove
        vector_zero = numpy.subtract(zero, position)
        vector_floor = numpy.subtract(floor, position)

        # Orientation variables
        self.current_yaw = 0
        self.current_pitch = 0

        # TODO: Move these variables to a separate script inorder to make more generic
        self.__position = position
        self.__unit_vector_zero = vector_zero / numpy.linalg.norm(vector_zero)
        self.__unit_vector_floor = vector_floor / numpy.linalg.norm(vector_floor)

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

        self.current_yaw = new_yaw
        self.current_pitch = new_pitch

    # TODO: REMOVE AND PUT ELSEWHERE
    def look_at_coordinate(self, coordinate: numpy.array):
        # Vectors
        vector_coord = numpy.subtract(coordinate, self.__position)
        unit_vector_coord = vector_coord / numpy.linalg.norm(vector_coord)
        unit_vector_zero = self.__unit_vector_zero
        unit_vector_floor = self.__unit_vector_floor

        # Calculate which side of the room the person is at
        # side < 0 => bedroom side of the room
        # side > 0 => kitchen side of the room
        # https://math.stackexchange.com/questions/214187/point-on-the-left-or-right-side-of-a-plane-in-3d-space
        matrix = numpy.array([unit_vector_floor, unit_vector_zero, unit_vector_coord])
        side = numpy.linalg.det(matrix)

        # Calculate degrees for yaw
        dot_product = numpy.dot(unit_vector_coord, unit_vector_zero)
        rad_angle = numpy.arccos(dot_product)
        yaw_deg_angle = int(rad_angle * 180 / 3.1415)

        if side < 0:
            yaw_deg_angle = 360 - yaw_deg_angle

        # Calculate degrees for yaw
        dot_product = numpy.dot(unit_vector_coord, unit_vector_floor)
        rad_angle = numpy.arccos(dot_product)
        pitch_deg_angle = int(rad_angle * 180 / 3.1415)

        print("Yaw: " + str(yaw_deg_angle) + ", Pitch: " + str(pitch_deg_angle))

        self.rotate(yaw_deg_angle, pitch_deg_angle + 80)
