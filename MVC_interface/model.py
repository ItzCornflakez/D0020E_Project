from MVC_interface.controller import Controller
from observer_pattern.observer import Observer, Subject


class Model(Subject, Observer):
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def update(self, subject: Controller) -> None:

        #TODO-this may be fcked
        self.imgtk = subject.imgtk

        self.notify()
