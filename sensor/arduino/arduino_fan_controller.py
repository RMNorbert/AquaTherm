import serial
import time


class ArduinoFanController:
    def __init__(self, port='COM6', baud_rate=115200):
        self.port = port
        self.baud_rate = baud_rate
        self.ser_f = None
        self.fanStatus = 'Fan: turned off'

    def connect(self):
        self.ser_f = serial.Serial(self.port, self.baud_rate, timeout=1)

    def disconnect(self):
        if self.ser_f is not None:
            self.ser_f.close()
            self.ser_f = None

    def is_connected(self):
        return self.ser_f is not None

    def switch_fan(self, command):
        retries = 3
        while retries > 0:
            try:
                if self.ser_f is None:
                    self.connect()

                my_command = command + '\r'
                self.ser_f.write(my_command.encode())

                if command == "off":
                    self.disconnect()

                self.fanStatus = f'Fan: turned {command}'
                return self.fanStatus

            except RuntimeError as error:
                print(error.args[0])
                time.sleep(2.0)
                retries -= 1

            except Exception as error:
                self.disconnect()
                raise error

        return self.fanStatus
