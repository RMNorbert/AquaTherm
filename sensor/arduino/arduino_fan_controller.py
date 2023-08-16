# to use pip install pyserial
import serial
import time
# 1st step : To set Arduino -> tools -> manage libraries -> search the corresponding to the device if there is any ,
# install the package
# 2nd step : file -> samples -> select the sensor
# 3rd step: Use Arduino IDE to upload the firmware onto the arduino board
# or create a custom fan controller in Arduino Ide with this code
# An example setup:
# General IRF530 N to 100 V 17 a to 220 N Channel Transistor Mosfet
# Arctic ACFAN00118A Fan
# Arduino Uno
# sd card
# set the port and baud rate


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
