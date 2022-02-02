from tkinter.ttk import *
from tkinter import ttk
from MVC_interface.model import Model

from observer_pattern.observer import Observer


class View(ttk.Frame, Observer):
    def __init__(self, parent):
        super().__init__(parent)
        self.old_value = 0
        

        #Define column sizes
        self.columnconfigure(0,weight=10)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)
        self.columnconfigure(3,weight=1)

        #Define row sizes
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        #StyleSheet for buttons
        style = Style()
        style.configure(style="BW.TButton", foreground="black", background="white")
        style.configure(style="S.TLabel", font=("Arial", 25))

        app = Frame()
        app.grid()
        self.lmain = Label(app)
        self.lmain.grid()

        title = Label(text="Interface for Camera", style="S.TLabel")
            
        #inputs for rotate button
        rotate_Input1 = Entry(style="TEntry", width=5)
        rotate_Input2 = Entry(style="TEntry", width=5)

        def rotate_cam():
                
            self.controller.rotate(int(rotate_Input1.get()), int(rotate_Input2.get()))
            self.controller.is_follow = False


        rotate_Button = Button(text="rotate Camera", command=rotate_cam, style="BW.TButton")

        
        def lookAtWideFind():
            self.val = self.look_at_person_dropdown.get()
            self.controller.lookAtWideFind(self.val)
            self.controller.is_follow = False

        def followWideFind():
            self.val = self.follow_person_dropdown.get()
            if not self.controller.is_follow:
                self.controller.is_follow = True
            else:
                if self.val != self.old_value:
                    pass
                else:
                    self.controller.is_follow = False
            
            self.old_value = self.val

        self.follow_person_dropdown = Combobox()
        self.follow_person_Button = Button(text="Follow person",command=followWideFind, style="BW.TButton")

        #TODO-use below for look at person functionality
        self.look_at_person_dropdown = Combobox()
        self.look_person_Button = Button(text="Look at person", command=lookAtWideFind, style="BW.TButton")

        #TODO-use below for look at object functionality
        look_at_object_dropdown = Combobox(values=['microoven', 'oven'])
        look_object_Button = Button(text="Look at object", style="BW.TButton")

        disc_Button = Button(text="Disconnect", command=lambda: self.quit(), style="BW.TButton")

        #Place on grid
        title.grid(row=0, column=0)
        app.grid(row=1, column=0, rowspan=4)
        rotate_Input1.grid(row=0, column=1)
        rotate_Input2.grid(row=0, column=2)
        rotate_Button.grid(row=0, column=3)

        # follow_Button.grid(row=1, column=2)

        self.follow_person_dropdown.grid(row=1, column=2)
        self.follow_person_Button.grid(row=1, column=3)

        self.look_at_person_dropdown.grid(row=2, column=2)
        self.look_person_Button.grid(row=2, column=3)

        look_at_object_dropdown.grid(row=3, column=2)
        look_object_Button.grid(row=3, column=3)

        disc_Button.grid(row=4, column=2)


        self.controller = None


    def set_controller(self, controller):
            """
            Set the controller
            :param controller:
            :return:
            """
            self.controller = controller
    

    def update(self, subject: Model) -> None:
        """
        Receive update from subject.
        """
        self.lmain.configure(image=subject.imgtk)
        self.lmain.imgtk = subject.imgtk

        self.follow_person_dropdown['values'] = subject.trackers
        self.look_at_person_dropdown['values'] = subject.trackers
