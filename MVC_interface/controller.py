from observer_pattern.observer import Observer, Subject
from video_get import VideoGet
from video_show import VideoShow
import threading
import time

from widefind import WideFind

class Controller(Subject, Observer):
    def __init__(self, parent, model, view):
        self.model = model
        self.view = view
        self.cam = parent.cam
        self.cam_trans = parent.cam_trans
        self.trackers = []
        self.trackersDict = {}
        self._observers = []
        self.video_getter = VideoGet(parent.src).start()
        self.video_shower = VideoShow(self.video_getter.frame, parent.screen_width, parent.screen_height).start()
        t1 = threading.Thread(target=self.changeFrameLoop)
        t1.daemon = True
        t1.start()

        self.is_follow = False


    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def changeFrameLoop(self):
        while(True):
            frame = self.video_getter.frame
            self.video_shower.frame = frame
            self.imgtk = self.video_shower.imgtk
            self.notify()
    
    def rotate(self, i, j):
        self.cam.rotate(i, j)

    def lookAtWideFind(self, val):
            if val in self.trackers:
                tracker_pos = self.trackersDict[val]
                new_yaw = self.cam_trans.get_yaw_from_zero(tracker_pos)
                new_pitch = self.cam_trans.get_pitch_from_zero(tracker_pos)

                self.cam.rotate(new_yaw, new_pitch + 80)

    def update(self, subject: WideFind):

        self.trackersDict = subject.trackers
        
        for tracker in subject.trackers:
            if tracker not in self.trackers:
                self.trackers.append(tracker)
        if self.is_follow:
            self.lookAtWideFind(self.view.val)
        
        self.notify()