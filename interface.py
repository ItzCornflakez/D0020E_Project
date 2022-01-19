from tkinter import *
from tkinter.ttk import *
from turtle import width
from camera import HDIntegratedCamera
from transform import Vector3

class interface:

    def __init__(self):
        self.createInterface()

    def createInterface(self):
        root = Tk()
        #Define Window
        root.geometry('1440x900')
        root.resizable(0,0)
        root.title('Camera Interface')

        #Define column sizes
        root.columnconfigure(0,weight=50)
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
        
        #TODO-Placeholder for camera feed
        l1 = Label(text="camera feed goes here")
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
        l1.grid(row=0, column=0)
        rotate_Input1.grid(row=0, column=1)
        rotate_Input2.grid(row=0, column=2)
        rotate_Button.grid(row=0, column=3)

        

        follow_Button.grid(row=1, column=2)

        dropDownList.grid(row=2, column=2)
        #look_Button.grid(row=2, column=2)

        disc_Button.grid(row=3, column=2)
        
        root.mainloop()