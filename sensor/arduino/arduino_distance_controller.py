import serial
import time


class ArduinoDistanceController:
    def __init__(self, port='COM13', baud_rate=115200):  # set the port and baud rate
        self.port = port
        self.baud_rate = baud_rate
        self.ser_d = None
        self.distance = 0

    def connect(self):
        self.ser_d = serial.Serial(self.port, self.baud_rate, timeout=1)

    def disconnect(self):
        if self.ser_d is not None:
            self.ser_d.close()
            self.ser_d = None

    def get_distance(self):
        retries = 5
        while retries > 0:
            try:
                if self.ser_d is None:
                    self.connect()

                line = self.ser_d.readline().decode("utf-8").split(",")

                self.distance = int(line[1])

                return (self.distance)

            except RuntimeError as error:
                print(error.args[0])
                time.sleep(2.0)
                retries -= 1

            except Exception as error:
                self.disconnect()  # Close the port on any other exception
                raise error

        return (self.distance)