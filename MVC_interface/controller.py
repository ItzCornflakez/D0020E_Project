from observer_pattern.observer import Observer, Subject
from video_get import VideoGet
from video_show import VideoShow
import threading

class Controller(Subject):
    def __init__(self, parent, model, view):
        self.model = model
        self.view = view
        self._observers = []
        self.video_getter = VideoGet(parent.src).start()
        self.video_shower = VideoShow(self.video_getter.frame, parent.screen_width, parent.screen_height).start()
        t1 = threading.Thread(target=self.changeFrame)
        t1.daemon = True
        t1.start()


    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.pop(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def changeFrame(self):
        while(True):
            frame = self.video_getter.frame
            self.video_shower.frame = frame
            self.imgtk = self.video_shower.imgtk
            print("hello")
            self.notify()
