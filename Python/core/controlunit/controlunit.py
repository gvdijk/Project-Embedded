from enum import Enum

from Python.core.controlunit.connection import Connector


class ControlUnit:
    pass

    class Type(Enum):
        LIGHT = 1
        TEMPERATURE = 2

    def __init__(self, unit_type: Type, connector: Connector):
        print('Initializing class Control unit of type ' + unit_type.__str__())
        self.type = unit_type
        self.id = id
        self.data = []
        self.connector = connector

    def add_data(self, value):
        self.data.append(value)
