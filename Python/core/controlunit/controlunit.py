from enum import Enum


class ControlUnit:
    pass

    class Type(Enum):
        LIGHT = 1
        TEMPERATURE = 2

    def __init__(self, type: Type):
        self.type = type
