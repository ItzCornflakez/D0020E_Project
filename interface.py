from tkinter import Tk, Label, Button
from tkinter.ttk import *
from turtle import width
from camera import HDIntegratedCamera
from transform import Vector3
from PIL import ImageTk, Image
from video_get import VideoGet
from video_show import VideoShow
import threading
import cv2
import time
import numpy


class interface: 

    def __init__(self, src):
        self.createInterface(src)

        camera_pos = numpy.array([950, 3500, 3000])
        camera_zero = numpy.array([-100, 4000, 2000])

        self.hd_cam = HDIntegratedCamera("http://130.240.105.145/cgi-bin/aw_ptz?cmd=%23", camera_pos, camera_zero)


    def createInterface(self, src):
        root = Tk()
        #Define Window
        root.geometry('640x480')
        root.attributes('-fullscreen', True)

        root.resizable(0,0)
        root.title('Camera Interface')

        #Define column sizes
        root.columnconfigure(0,weight=10)
        root.columnconfigure(1,weight=1)
        root.columnconfigure(2,weight=1)
        root.columnconfigure(3,weight=1)

        #Define row sizes
        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        root.rowconfigure(2, weight=1)
        root.rowconfigure(3, weight=1)

        #StyleSheet for buttons
        style = Style()
        style.configure(style="BW.TButton", foreground="black", background="white")

        #Creates a frame that the video feed from camera is put in
        app = Frame()
        app.grid()
        # Create a label in the frame
        lmain = Label(app)
        lmain.grid()

        #TODO (this does not work very well unless threading is used(i think), camera lags,
        #  work in progress)
        

        #function that calls 2 separate threads that read and writes the frames from camera respectivly

        #video_getter = VideoGet(src).start()
        #video_shower = VideoShow(video_getter.frame).start()
        
        cap = cv2.VideoCapture(src)
       

        def frame_loop():
            
            _, frame = cap.read()
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            img = img.resize((740,500), Image.ANTIALIAS)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
            lmain.after(10,frame_loop)
        
        t1 = threading.Thread(target=frame_loop).start()
        
        #inputs for rotate button
        rotate_Input1 = Entry(style="TEntry", width=5)
        rotate_Input2 = Entry(style="TEntry", width=5)

        def rotate():
                r_I1 = int(rotate_Input1.get())
                r_I2 = int(rotate_Input2.get())

                
                self.hd_cam.rotate(r_I1, r_I2)
            
        #Create Buttons
        rotate_Button = Button(text="rotate Camera", command=rotate, style="BW.TButton")
        follow_Button = Button(text="Follow person", style="BW.TButton")
        disc_Button = Button(text="Disconnect", command=lambda: root.quit(), style="BW.TButton")

        #Place on grid
        app.grid(row=0, column=0)
        rotate_Input1.grid(row=0, column=1)
        rotate_Input2.grid(row=0, column=2)
        rotate_Button.grid(row=0, column=3)

        follow_Button.grid(row=1, column=2)

        disc_Button.grid(row=3, column=2)

        # Create a frame

        root.mainloop()

        