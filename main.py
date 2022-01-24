import time
import numpy

from camera import HDIntegratedCamera
from transform import Vector3
from widefind import WideFind

# This is a makeshift test script.
# Meant to be replaced by a proper interface.

debug = False

# 17C08B1230924C5D
camera_bedroom_pos = numpy.array([1162, 3335, 2326])
camera_bedroom_zero = numpy.array([133, 3628, 2193])
camera_bedroom_floor = numpy.array([632, 3378,  597])

camera_kitchen_pos = numpy.array([2873, -2602,  2186])
camera_kitchen_zero = numpy.array([3413, -2722,  2284])
camera_kitchen_floor = numpy.array([2694, -2722, 193])

# camera_bedroom = HDIntegratedCamera("http://130.240.105.145/cgi-bin/aw_ptz?cmd=%23", camera_bedroom_pos, camera_bedroom_zero, camera_bedroom_floor)
camera_kitchen = HDIntegratedCamera("http://130.240.105.144/cgi-bin/aw_ptz?cmd=%23", camera_kitchen_pos, camera_kitchen_zero, camera_kitchen_floor)

widefind = WideFind("130.240.74.55", 1883)
widefind.run(debug)

while True:
    time.sleep(.2)

    if "F1587D88122BE247" in widefind.trackers:
        print(widefind.trackers["F1587D88122BE247"])
        camera_kitchen.look_at_coordinate(widefind.trackers["F1587D88122BE247"])
