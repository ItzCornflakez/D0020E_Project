from interface import interface
import time
import cv2

src = "rtsp://130.240.105.144:554/mediainput/h264/stream_1"
# src = 0

intface = interface(src)

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
