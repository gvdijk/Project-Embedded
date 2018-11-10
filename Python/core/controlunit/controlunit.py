from enum import Enum

from Python.core.controlunit.connection import Connector


class ControlUnit:
    pass

    class Type(Enum):
        LIGHT = 1
        TEMPERATURE = 2
        UNIDENTIFIED = 10

    def __init__(self, unit_type: Type = Type.UNIDENTIFIED):
        print('Initializing class Control unit of type ' + unit_type.__str__())
        self.type = unit_type
        self.id = id
        self.data = []

    def add_data(self, value):
        self.data.append(value)
