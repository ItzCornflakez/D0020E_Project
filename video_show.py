from threading import Thread
import cv2
from PIL import ImageTk, Image

class VideoShow:

    #Class that continously shows frames from camera with a dedicated thread

    def __init__(self, frame):
        self.frame = frame
        cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        img = img.resize((740,500), Image.ANTIALIAS)
        self.imgtk = ImageTk.PhotoImage(image=img)
    
    def start(self):
        t3 = Thread(target=self.process)
        t3.daemon = True
        t3.start()
        return self

    def process(self):
        while True:
            cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            img = img.resize((740,500), Image.ANTIALIAS)
            self.imgtk = ImageTk.PhotoImage(image=img)






