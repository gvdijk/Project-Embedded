import asyncio
import time
from threading import Thread

import serial.tools.list_ports

from Python.core.controlunit.controlunit import ControlUnit
from Python.event.event import Event


class ControlUnitFinder:
    class ControlUnitFoundEvent(Event):
        def __init__(self, global_identifier: str):
            super().__init__(global_identifier)

    def __init__(self):
        self.control_units = {}
        self.control_unit_found_event = ControlUnitFinder.ControlUnitFoundEvent('control_unit_found')

    def poll(self):
        ports_found = serial.tools.list_ports.comports()

        for port in ports_found:

            def check_type(deviceport):
                try:
                    control_unit = ControlUnit(deviceport.device)
                    time.sleep(2)
                    control_unit.type = control_unit.get_sensor_type()

                    if control_unit.type is not ControlUnit.Type.UNIDENTIFIED:
                        self.control_units[deviceport.device] = control_unit
                        self.control_unit_found_event.call(control_unit=control_unit)
                except:
                    print("already connected {} and {}".format(port.device, self.control_units.keys()))

            if port.device not in self.control_units.keys():
                thread = Thread(target=check_type(port)).start()

    def remove_control_unit(self, control_unit):
        self.control_units.pop(control_unit.port)
