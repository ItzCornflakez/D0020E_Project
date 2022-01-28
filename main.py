import time
from camera import HDIntegratedCamera
import widefind as wf
import numpy as np

# This is a makeshift test script.
# Meant to be replaced by a proper interface.

# 17C08B1230924C5D
# camera_bedroom_pos = numpy.array([1162, 3335, 2326])
# camera_bedroom_zero = numpy.array([133, 3628, 2193])
# camera_bedroom_floor = numpy.array([632, 3378,  597])

camera_kitchen_pos = np.array([2873, -2602,  2186])
camera_kitchen_zero = np.array([3413, -2722,  2284])
camera_kitchen_floor = np.array([2694, -2722, 193])

widefind = wf.WideFind("130.240.74.55", 1883)
widefind.run("ltu-system/#", False)

kit_cam_trans = wf.Transform(camera_kitchen_pos, camera_kitchen_zero, camera_kitchen_floor)

# camera_bedroom = HDIntegratedCamera("http://130.240.105.145/cgi-bin/aw_ptz?cmd=%23")
camera_kitchen = HDIntegratedCamera("http://130.240.105.144/cgi-bin/aw_ptz?cmd=%23")


while True:
    time.sleep(.2)

    if "F1587D88122BE247" in widefind.trackers:
        print(widefind.trackers["F1587D88122BE247"])

        newYaw = kit_cam_trans.get_yaw_from_zero(widefind.trackers["F1587D88122BE247"])
        newPitch = kit_cam_trans.get_pitch_from_zero(widefind.trackers["F1587D88122BE247"])
        camera_kitchen.rotate(newYaw, newPitch + 80)
