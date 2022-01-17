from camera import HDIntegratedCamera
from transform import Vector3

# This is a makeshift test script.
# Meant to be replaced by a proper interface.

cameraPosition = Vector3(3261, -3800, 740)
cameraFloorPosition = Vector3(3635, -4074, 418)  # WHAT HOW IS THIS THE FLOOR POSITION OF CAMERA MAKES NO SENSE

camera = HDIntegratedCamera("http://130.240.105.145/cgi-bin/aw_ptz?cmd=%23", cameraPosition)
print("Note: Arguments should be given as integers")

while True:
    print("Give new arguments to camera:")
    newYaw = int(input("Yaw: "))
    newPitch = int(input("Pitch: "))

    camera.rotate(newYaw, newPitch)
    print("-----------------------------")