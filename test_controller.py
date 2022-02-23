from camera import HDIntegratedCamera
from observer_pattern.observer import Observer, Subject
import numpy

from widefind import WideFind
import widefind as wf


class Controller(Observer):
    def __init__(self):

        camera_bedroom_pos = numpy.array([619, 3935, 2600])
        camera_bedroom_zero = numpy.array([-765, 4112, 2878])
        camera_bedroom_floor = numpy.array([531, 3377, 331])

        self.cam = HDIntegratedCamera("http://130.240.105.144/cgi-bin/aw_ptz?cmd=%23")
        self.cam_trans = wf.Transform(camera_bedroom_pos, camera_bedroom_zero, camera_bedroom_floor)
        self.trackers = []
        self.trackersDict = {}

        self.is_follow = False

    def rotate(self, i, j):
        self.cam.rotate(i, j)

    
    def update(self, subject: WideFind):
        self.trackersDict = subject.trackers
        self.trackers = subject.trackers.keys()
        
