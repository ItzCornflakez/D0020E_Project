from threading import Thread
import cv2
from PIL import ImageTk, Image

class VideoShow:

    #Class that continously shows frames from camera with a dedicated thread

    def __init__(self, frame):
        self.frame = frame
    
    def start(self):
        t2 = Thread(target=self.show, args=()).start()
        return self

    def show(self):
        while True:
            # cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)
            # img = Image.fromarray(cv2image)
            # img = img.resize((320,220), Image.ANTIALIAS)
            # imgtk = ImageTk.PhotoImage(image=img)
            # lmain.imgtk = imgtk
            # lmain.configure(image=imgtk)
            cv2.imshow("Video", self.frame)





