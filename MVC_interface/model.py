from MVC_interface.view import View
from observer_pattern.observer import Observer, Subject


class Model(Subject, Observer):
    def _init_(self):
        self.observers = []



    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass

    def update(self, subject: View) -> None:
        """
        Receive update from subject.
        """
        pass
