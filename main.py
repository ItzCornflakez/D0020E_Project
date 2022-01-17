from camera import HDIntegratedCamera

# This is a makeshift test script.
# Meant to be replaced by a proper interface.

camera = HDIntegratedCamera("http://130.240.105.145/cgi-bin/aw_ptz?cmd=%23")
print("Note: Arguments should be given as integers")

while True:
    print("Give new arguments to camera:")
    newYaw = int(input("Yaw: "))
    newPitch = int(input("Pitch: "))

    camera.rotate(newYaw, newPitch)
    print("-----------------------------")
