#from interface import interface
import numpy
from camera import HDIntegratedCamera
import widefind as wf
import tkinter as tk
from MVC_interface.controller import Controller
from MVC_interface.model import Model
from MVC_interface.view import View
from observer_pattern.observer import Observer
from video_get import VideoGet
from video_show import VideoShow
import time

src = "rtsp://130.240.105.145:554/mediainput/h264/stream_1"
#src = 0

camera_bedroom_pos = numpy.array([1162, 3335, 2326])
camera_bedroom_zero = numpy.array([133, 3628, 2193])
camera_bedroom_floor = numpy.array([632, 3378,  597])
        
camera_kitchen_pos = numpy.array([2873, -2602,  2186])
camera_kitchen_zero = numpy.array([3413, -2722,  2284])
camera_kitchen_floor = numpy.array([2694, -2722, 193])

cam = HDIntegratedCamera("http://130.240.105.145/cgi-bin/aw_ptz?cmd=%23")
widefind = wf.WideFind("130.240.74.55", 1883)
widefind.run("ltu-system/#", False)

kit_cam_trans = wf.Transform(camera_bedroom_pos, camera_bedroom_zero, camera_bedroom_floor)
#kit_cam_trans = wf.Transform(camera_kitchen_pos, camera_kitchen_zero, camera_kitchen_floor)

#intface = interface(src, cam, kit_cam_trans, widefind)
#widefind.attach(interface)


class main(tk.Tk):
    def __init__(self):
        super().__init__()

        #Start conditions
        self.src = src
        self.cam = cam
        self.cam_trans = kit_cam_trans
        self.geometry('640x480')
        self.attributes('-fullscreen', True)
        self.resizable(0,0)
        self.title('Camera Interface')
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        

        model = Model()
        
        view = View(self)
        controller = Controller(self, model, view)
        view.set_controller(controller)


        model.attach(view)
        controller.attach(model)
        widefind.attach(controller)

if __name__ == '__main__':
    m = main()
    m.mainloop()
    

        

        



