import threading
import time

import serial.tools.list_ports

from Python.core.controlunit.connection import Connector
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

            def call_event():
                connector = Connector(port.device)
                time.sleep(2)
                t = connector.readSensorType()

                if t is not None:
                    connector.connection_lost_event.add_listener(self.on_connection_lost)

                    control_unit = ControlUnit(ControlUnit.Type(t), connector)
                    self.control_units[port.device] = control_unit
                    self.control_unit_found_event.call(control_unit=control_unit)

            if port.device not in self.control_units.keys():
                thread = threading.Thread(target=call_event)
                thread.start()


    def on_connection_lost(self, event_data):
        connector = event_data['connector']
        print(connector)




















    # def poll_ports(self):
    #     print('polling')
    #     ports_found = serial.tools.list_ports.comports()
    #
    #     def add_port(port):
    #         print('adding')
    #         con: Connector = Connector(port.device)
    #         time.sleep(2)
    #         type = con.readSensorType()
    #         print('type')
    #         print(type)
    #         if type is not None:
    #             ports[port.device] = (con, port.serial_number)
    #             print("Port {} successfully verified as {} with id {} \n".format(port.device, type, port.serial_number))
    #             print('maxDistance')
    #             print(con.readMinDistance())
    #             print('inDistance')
    #             print(con.readMaxDistance())
    #
    #     for port in ports_found:
    #         if port.device not in ports.keys():
    #             add_port(port)
    #         elif ports[port.device][1] != port.serial_number:
    #             ports[port.device][0].close()
    #             add_port(port)
