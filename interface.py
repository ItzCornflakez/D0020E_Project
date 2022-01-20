from tkinter import Tk, Label, Button
from tkinter.ttk import *
from turtle import width
from camera import HDIntegratedCamera
from transform import Vector3
import cv2
from PIL import ImageTk, Image
import VideoGet
import VideoShow

class interface: 

    def __init__(self, src):
        self.createInterface(src)

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
        
        def ThreadBoth(src):

            #function that calls 2 separate threads that read and writes the frames from camera respectivly

            video_getter = VideoGet(src).start()
            video_shower = VideoShow(video_getter.frame).start()

            while True:
                if video_getter.stopped or video_shower.stopped:
                    video_shower.stop()
                    video_getter.stop()
                    break
                
                frame = video_getter.frame
                video_shower.frame = frame
        
        ThreadBoth(src)
        
        #inputs for rotate button
        rotate_Input1 = Entry(style="TEntry", width=5)
        rotate_Input2 = Entry(style="TEntry", width=5)

        #Create Buttons
        rotate_Button = Button(text="rotate Camera", style="BW.TButton")
        look_Button= Button(text="Look at position", style="BW.TButton")
        follow_Button = Button(text="Follow person", style="BW.TButton")
        disc_Button = Button(text="Disconnect", command=lambda: root.quit(), style="BW.TButton")

        #TODO-Placeholder feature for look at position
        dropDownList = Combobox(values=["Fridge", "Sofa", "Tv"])

        #Place on grid
        app.grid(row=0, column=0, sticky="nesw")
        rotate_Input1.grid(row=0, column=1)
        rotate_Input2.grid(row=0, column=2)
        rotate_Button.grid(row=0, column=3)

        

        follow_Button.grid(row=1, column=2)

        dropDownList.grid(row=2, column=2)
        #look_Button.grid(row=2, column=2)

        disc_Button.grid(row=3, column=2)

        # Create a frame

        root.mainloop()

        