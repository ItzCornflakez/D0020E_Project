from threading import Thread
import cv2
from PIL import ImageTk, Image

class VideoShow:

    #Class that continously shows frames from camera with a dedicated thread

    def __init__(self, frame, width, height):
        self.frame = frame
        self.adj_width = (int)(width/1.5)
        self.adj_height = (int)(height/1.5)
        cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        img = img.resize((self.adj_width,self.adj_height), Image.ANTIALIAS)
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
            #img = img.resize((740,500), Image.ANTIALIAS)
            img = img.resize((self.adj_width,self.adj_height), Image.ANTIALIAS)
            self.imgtk = ImageTk.PhotoImage(image=img)






