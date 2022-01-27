from interface import interface
import time
import cv2
import numpy
from camera import HDIntegratedCamera
from widefind import WideFind

src = "rtsp://130.240.105.145:554/mediainput/h264/stream_1"
#src = 0

camera_bedroom_pos = numpy.array([1162, 3335, 2326])
camera_bedroom_zero = numpy.array([133, 3628, 2193])
camera_bedroom_floor = numpy.array([632, 3378,  597])
        

cam = HDIntegratedCamera("http://130.240.105.145/cgi-bin/aw_ptz?cmd=%23", camera_bedroom_pos, camera_bedroom_zero, camera_bedroom_floor)
widefind = WideFind("130.240.74.55", 1883)
widefind.run(False)
intface = interface(src, cam, widefind)

# cap = cv2.VideoCapture(src)

# while(True):
#     start = time.time()
#     ret, frame = cap.read()
#     end = time.time()
#     print("this is first:" + (str)(end-start))
#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break
