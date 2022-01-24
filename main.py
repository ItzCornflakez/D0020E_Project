import time
import numpy

from camera import HDIntegratedCamera
from transform import Vector3
from widefind import WideFind

# This is a makeshift test script.
# Meant to be replaced by a proper interface.

debug = False

# 17C08B1230924C5D
camera_pos = numpy.array([950, 3500, 3000])
camera_zero = numpy.array([-100, 4000, 2000])

camera = HDIntegratedCamera("http://130.240.105.145/cgi-bin/aw_ptz?cmd=%23", camera_pos, camera_zero)

widefind = WideFind("130.240.74.55", 1883)
widefind.run(debug)

while True:
    time.sleep(3)
    camera.absolute_rotate(0, 180)
    # camera.look_at_coordinate(numpy.array([1, 1, 0]))

    if "F1587D88122BE247" in widefind.trackers:
        print(numpy.linalg.norm(numpy.subtract(widefind.trackers["F1587D88122BE247"], camera_pos)))
        # camera.look_at_coordinate(widefind.trackers["F1587D88122BE247"])
