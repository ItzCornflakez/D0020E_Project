from threading import Thread
import cv2

class VideoGet:

    #Class that continously gets frames from camera with a dedicated thread

    def __init__(self, src):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        
    
    def start(self):
        t2 = Thread(target=self.get)
        t2.daemon = True
        t2.start()
        return self

    def get(self):
        while True:
            (self.grabbed, self.frame) = self.stream.read()





