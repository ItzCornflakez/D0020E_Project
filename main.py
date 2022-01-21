import time

from camera import HDIntegratedCamera
from transform import Vector3
from widefind import WideFind
from personlook import  Personlook
import numpy


# This is a makeshift test script.
# Meant to be replaced by a proper interface.

debug = True

#cameraPosition = Vector3(3261, -3800, 740)
#cameraFloorPosition = Vector3(3635, -4074, 418)  # WHAT HOW IS THIS THE FLOOR POSITION OF CAMERA MAKES NO SENSE
#cameraPosition = Personlook().positioner()
#cameraFloorPosition = Personlook().positioner()
#camera = HDIntegratedCamera("http://130.240.105.145/cgi-bin/aw_ptz?cmd=%23",[628,3340,2775],[489,3745,1409])
#camera.absoluteRotate(360,150)

camera_pos = numpy.array([628,3340,2775])
camera_zero = numpy.array([489,3745,1409])
camera = HDIntegratedCamera("http://130.240.105.145/cgi-bin/aw_ptz?cmd=%23",camera_pos,camera_zero)


#widefind = WideFind("130.240.105.144", 1883)
#widefind.run(debug)

#while True:
#    time.sleep(2)
