from observer_pattern.observer import Observer


class Model(Observer):
    def _init_(self):
        print("model")
