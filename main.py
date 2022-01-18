import time

from camera import HDIntegratedCamera
from transform import Vector3
from widefind import WideFind

# This is a makeshift test script.
# Meant to be replaced by a proper interface.

debug = True

cameraPosition = Vector3(3261, -3800, 740)
cameraFloorPosition = Vector3(3635, -4074, 418)  # WHAT HOW IS THIS THE FLOOR POSITION OF CAMERA MAKES NO SENSE

widefind = WideFind("130.240.74.55", 1883)
widefind.run(debug)

while True:
    time.sleep(2)
