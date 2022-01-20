from threading import Thread
import cv2

class VideoGet:

    #Class that continously gets frames from camera with a dedicated thread

    def __init__(self, src):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        
    
    def start(self):
        t1 = Thread(target=self.get, args=()).start()
        return self

    def get(self):
        while True:
            (self.grabbed, self.frame) = self.stream.read()





