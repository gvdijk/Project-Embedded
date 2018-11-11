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
        print('polling')
        ports_found = serial.tools.list_ports.comports()

        for port in ports_found:

            def check_type():
                control_unit = ControlUnit(port.device)
                time.sleep(2)
                control_unit.type = control_unit.get_sensor_type()

                if control_unit.type is not ControlUnit.Type.UNIDENTIFIED:
                    control_unit.connection_lost_event.add_listener(self.on_connection_lost)
                    self.control_units[port.device] = control_unit
                    self.control_unit_found_event.call(control_unit=control_unit)

            if port.device not in self.control_units.keys():
                thread = Thread(target=check_type).start()

    def on_connection_lost(self, event_data):
        unit = event_data['control_unit']
        if unit.port in self.control_units:
            self.control_units.pop(unit.port)
