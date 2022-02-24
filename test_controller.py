from camera import HDIntegratedCamera
from observer_pattern.observer import Observer, Subject
import numpy
import cv2
from video_get import VideoGet

from widefind import WideFind
import widefind as wf


class Controller(Observer):
    def __init__(self):

        camera_bedroom_pos = numpy.array([619, 3935, 2600])
        camera_bedroom_zero = numpy.array([-765, 4112, 2878])
        camera_bedroom_floor = numpy.array([531, 3377, 331])

        camera_kitchen_pos = numpy.array([2873, -2602, 2186])
        camera_kitchen_zero = numpy.array([3413, -2722, 2284])
        camera_kitchen_floor = numpy.array([2694, -2722, 193])

        self.cam = HDIntegratedCamera("http://130.240.105.144/cgi-bin/aw_ptz?cmd=%23")
        self.cam_trans = wf.Transform(camera_kitchen_pos, camera_kitchen_zero, camera_kitchen_floor)
        self.trackers = []
        self.trackersDict = {}
        self.video_getter = VideoGet("rtsp://130.240.105.144:554/mediainput/h264/stream_1").start()

        self.followTarget = ""

        self.is_follow = False

    def rotate(self, i, j):
        self.cam.rotate(i, j)

    def lookAtWideFind(self, val):
        if val in self.trackers:
            tracker_pos = self.trackersDict[val]
            new_yaw = self.cam_trans.get_yaw_from_zero(tracker_pos)
            new_pitch = self.cam_trans.get_pitch_from_zero(tracker_pos)

            self.cam.rotate(new_yaw, new_pitch + 80)

    def followWideFind(self, val):
        self.followTarget = val

    def changeFrameLoop(self):
        while True:
            frame = self.video_getter.frame
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    
    def update(self, subject: WideFind):
        self.trackersDict = subject.trackers
        self.trackers = subject.trackers.keys()
        if(self.is_follow == True):
            if(self.followTarget in self.trackers):
                self.lookAtWideFind(self.followTarget)
        
