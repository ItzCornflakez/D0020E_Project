from tkinter import *
from tkinter.ttk import *
from camera import HDIntegratedCamera
from transform import Vector3

class interface:

    def __init__(self):
        self.createInterface()

    def createInterface(self):
        root = Tk()

        style = Style()
        style.configure(style="BW.TLabel", foreground="black", background="white")

        l1 = Label(text="Interface", style="BW.TLabel")
        l1.pack()

        b1 = Button(text="rotate Camera", style="BW.TLabel")
        b1.pack(side="left")
        b2 = Button(text="Look at place", style="BW.TLabel")
        b2.pack(side="left")
        b3 = Button(text="Follow person", style="BW.TLabel")
        b3.pack(side="left")
        disconnect_Button = Button(text="Disconnect", command=lambda: root.quit(), style="BW.TLabel")
        disconnect_Button.pack()
        
        root.mainloop()