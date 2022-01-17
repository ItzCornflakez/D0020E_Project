class Transform:
    """Contains values and functions for calculating transformations in three-dimensional space"""
    def __init__(self):
        self.position = Vector3()
        self.eulerAngle = Vector3()


class Vector3:
    """Three-dimensional vector"""

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def toList(self):
        """Returns a list containing [x, y, z] elements of Vector."""
        return [self.x, self.y, self.z]

