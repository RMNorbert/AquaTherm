import serial
import time


class ArduinoTapController:
    def __init__(self, port='COM7', baud_rate=115200):  # set the port and baud rate
        self.port = port
        self.baud_rate = baud_rate
        self.ser_t = None
        self.tapStatus = 'Tap: turned off'

    def connect(self):
        self.ser_t = serial.Serial(self.port, self.baud_rate, timeout=1)

    def disconnect(self):
        if self.ser_t is not None:
            self.ser_t.close()
            self.ser_t = None

    def is_connected(self):
        return self.ser_t is not None

    def switch_tap(self, command):
        retries = 5
        while retries > 0:
            try:
                if self.ser_t is None:
                    self.connect()

                my_command = command + '\r'
                self.ser_f.write(my_command.encode())

                self.disconnect()
                self.tapStatus = f'Tap: turned {command}'
                return self.tapStatus

            except RuntimeError as error:
                print(error.args[0])
                time.sleep(2.0)
                retries -= 1

            except Exception as error:
                self.disconnect()
                raise error

        return self.tapStatus
