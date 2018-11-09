import time
from threading import Thread

import serial.tools.list_ports

from Python.core.controlunit.connection import Connector
from Python.core.controlunit.controlunit import ControlUnit
from Python.event.event import Event


class Engine:
    class ControlUnitAddedEvent(Event):
        def __init__(self):
            super().__init__('control_unit_added')

    class ControlUnitRemovedEvent(Event):
        def __init__(self):
            super().__init__('control_unit_removed')

    def __init__(self):
        print('Initializing class Engine')

        self.running = False
        self.__control_units = []
        self.on_control_unit_added = Engine.ControlUnitAddedEvent()
        self.on_control_unit_removed = Engine.ControlUnitRemovedEvent()

        self.thread = Thread(target=self.__tick)

    def add_control_unit(self, control_unit: ControlUnit):
        self.__control_units.append(control_unit)
        self.on_control_unit_added.call(control_unit=control_unit)

    def remove_control_unit(self, control_unit: ControlUnit):
        self.__control_units.remove(control_unit)
        self.on_control_unit_removed.call(control_unit=control_unit)

    def start(self):
        self.running = True
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()

    def __tick(self):
        while True:
            self.__poll_control_units()

    def __poll_control_units(self):
        print('polling')
        ports_found = serial.tools.list_ports.comports()
        ports = {}

        def add_port(port):
            print('adding')
            con: Connector = Connector(port.device)
            time.sleep(2)
            type = con.readSensorType()
            print('type')
            print(type)
            if type is not None:
                ports[port.device] = (con, port.serial_number)
                print("Port {} successfully verified as {} with id {} \n".format(port.device, type, port.serial_number))
                print('maxDistance')
                print(con.readMinDistance())
                print('inDistance')
                print(con.readMaxDistance())

        for port in ports_found:
            if port.device not in ports.keys():
                add_port(port)
            elif ports[port.device][1] != port.serial_number:
                ports[port.device][0].close()
                add_port(port)
