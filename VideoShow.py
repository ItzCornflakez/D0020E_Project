from threading import Thread
import cv2
from PIL import ImageTk, Image

class VideoGet:

    #Class that continously shows frames from camera with a dedicated thread

    def __init__(self, frame):
        self.frame = frame
        self.stopped = False
    
    def start(self):
        Thread(target=self.get, args=().start)
        return self

    def show(self, lmain):
        while not self.stopped:
            cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            img = img.resize((320,220), Image.ANTIALIAS)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)

    def stop(self):
        self.stopped = True





