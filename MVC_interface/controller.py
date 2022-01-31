from observer_pattern.observer import Observer, Subject

class Controller(Subject):
    def __init__(self, model, view):
        self.model = model
        self.view = view
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

    
