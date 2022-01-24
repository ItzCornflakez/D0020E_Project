from interface import interface
import cv2

src = "rtsp://130.240.105.144:554/mediainput/h264/stream_1"
#src = 0

intface = interface(src)

# cap = cv2.VideoCapture(src)

# while(True):
#     ret, frame = cap.read()
#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break
