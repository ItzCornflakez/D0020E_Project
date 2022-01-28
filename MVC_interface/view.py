from tkinter.ttk import *

class View(Frame):
    def _init(self):
        root = self.Tk
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

        app = Frame()
        app.grid()
        lmain = Label(app)
        lmain.grid()

        title = Label(text="Interface for Camera", style="S.TLabel")
            
        #inputs for rotate button
        rotate_Input1 = Entry(style="TEntry", width=5)
        rotate_Input2 = Entry(style="TEntry", width=5)

        rotate_Button = Button(text="rotate Camera", style="BW.TButton")

        follow_person_dropdown = Combobox()
        follow_person_Button = Button(text="Follow person", style="BW.TButton")
        

        #TODO-use below for look at person functionality
        look_at_person_dropdown = Combobox()
        look_person_Button = Button(text="Look at person", style="BW.TButton")

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
