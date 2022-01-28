from msilib.schema import ListBox
from tkinter import Tk, Label, Button, StringVar
from tkinter.ttk import *
from turtle import width
from transform import Vector3
from PIL import ImageTk, Image
from video_get import VideoGet
from video_show import VideoShow
import threading
import cv2
import time
from widefind import WideFind
from observer import Observer, Subject


class interface(Observer): 

    def __init__(self, src, cam, widefind):

        self.createInterface(src, cam, widefind)
        self.cam = cam
        self.widefind = widefind

    def update(self, subject: WideFind) -> None:
        """
        Receive update from subject.
        """
        pass



    def createInterface(self, src, cam, widefind):
        wideFindArray = []
        root = Tk()
        #Define Window
        root.geometry('640x480')
        root.attributes('-fullscreen', True)

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

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
        style.configure(style="S.TLabel", font=("Arial", 25))

        title = Label(text="Interface for Camera", style="S.TLabel")

        #Creates a frame that the video feed from camera is put in
        app = Frame()
        app.grid()
        # Create a label in the frame
        lmain = Label(app)
        lmain.grid()

        #TODO (this does not work very well unless threading is used(i think), camera lags,
        #  work in progress)
        

        #function that calls 2 separate threads that read and writes the frames from camera respectivly

        
        
        
        #cap = cv2.VideoCapture(src)
       

        def frame_loop():

            frame = video_getter.frame
            #_, frame = cap.read()
            video_shower.frame = frame
            imgtk = video_shower.imgtk
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
            
            # cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            # img = Image.fromarray(cv2image)
            # img = img.resize((740,500), Image.ANTIALIAS)
            # imgtk = ImageTk.PhotoImage(image=img)
            # lmain.imgtk = imgtk
            # lmain.configure(image=imgtk)
            lmain.after(10, frame_loop)

            follow_person_dropdown['values'] = wideFindArray
        
        
        
        #inputs for rotate button
        rotate_Input1 = Entry(style="TEntry", width=5)
        rotate_Input2 = Entry(style="TEntry", width=5)

        def rotate_cam():
                
                r_I1 = int(rotate_Input1.get())
                r_I2 = int(rotate_Input2.get())
                
                cam.rotate(r_I1, r_I2)
            
        #Create Buttons
        rotate_Button = Button(text="rotate Camera", command=rotate_cam, style="BW.TButton")
        

        def follow_person():
                time.sleep(0.4)
                look_at_person()

        def look_at_person():
            val = follow_person_dropdown.get()
            print(val)
            if val in widefind.trackers:
                print(widefind.trackers[val])
                cam.look_at_coordinate(widefind.trackers[val])
            

        def getWideFindArray():
            while(1):             
                trackers = widefind.trackers
                test = trackers.copy()

                for key in test.keys():
                    if(key not in wideFindArray):
                        wideFindArray.append(key)
                time.sleep(2)

        #TODO-use below for follow person functionality

        follow_person_dropdown = Combobox(values=wideFindArray)
        follow_person_Button = Button(text="Follow person", command=follow_person, style="BW.TButton")
        

        #TODO-use below for look at person functionality
        look_at_person_dropdown = Combobox(values=['first person', 'second person'])
        look_person_Button = Button(text="Look at person",command=look_at_person, style="BW.TButton")

        #TODO-use below for look at object functionality
        look_at_object_dropdown = Combobox(values=['microoven', 'oven'])
        look_object_Button = Button(text="Look at object", style="BW.TButton")

        disc_Button = Button(text="Disconnect", command=lambda: root.quit(), style="BW.TButton")

        #Place on grid
        title.grid(row=0, column=0)
        app.grid(row=1, column=0, rowspan=4)
        rotate_Input1.grid(row=0, column=1)
        rotate_Input2.grid(row=0, column=2)
        rotate_Button.grid(row=0, column=3)

        # follow_Button.grid(row=1, column=2)

        follow_person_dropdown.grid(row=1, column=2)
        follow_person_Button.grid(row=1, column=3)

        look_at_person_dropdown.grid(row=2, column=2)
        look_person_Button.grid(row=2, column=3)

        look_at_object_dropdown.grid(row=3, column=2)
        look_object_Button.grid(row=3, column=3)

        disc_Button.grid(row=4, column=2)

        #start threads and mainloop

        video_getter = VideoGet(src).start()
        video_shower = VideoShow(video_getter.frame, screen_width, screen_height).start()

        t2 = threading.Thread(target=getWideFindArray)
        t2.daemon = True
        t2.start()

        t1 = threading.Thread(target=frame_loop)
        t1.daemon = True
        t1.start()
        root.mainloop()

        