from typing import Callable


class Event:
    pass

    events = {}

    def __init__(self, name: str):
        self.__listeners = []
        self.name = name
        Event.events[name] = self

    def add_listener(self, listener: Callable):
        self.__listeners.append(listener)

    def remove_listener(self, listener: Callable):
        self.__listeners.remove(listener)

    def call(self, *args):
        for listener in self.__listeners:
            listener(args)
