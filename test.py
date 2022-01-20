from video_get import VideoGet
from video_show import VideoShow
import cv2

src = "rtsp://130.240.105.144:554/mediainput/h264/stream_1"
src = 0

def ThreadBoth(src):

            #function that calls 2 separate threads that read and writes the frames from camera respectivly

            video_getter = VideoGet(src).start()
            video_shower = VideoShow(video_getter.frame).start()

            while True:
                frame = video_getter.frame
                video_shower.frame = frame

ThreadBoth(src)

# cap = cv2.VideoCapture(src)

# while(True):
#     ret, frame = cap.read()
#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break
