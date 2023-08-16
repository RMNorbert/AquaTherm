import serial
import time


class ArduinoSensorController:
    def __init__(self, port='COM5', baud_rate=115200):  # set the port and baud rate
        self.port = port
        self.baud_rate = baud_rate
        self.ser_th = None
        self.isSensorOn = False
        self.temperature = 0.0
        self.humidity = 0.0
        self.tapStatus = 'Tap: turned off'
        self.fanStatus = 'Fan: turned off'

    def connect(self):
        if self.ser_th is None:
            self.ser_th = serial.Serial(self.port, self.baud_rate, timeout=1)

    def disconnect(self):
        if self.ser_th is not None:
            self.ser_th.close()
            self.ser_th = None

    def turn_sensor_on(self):
        command = 'on'
        self.ser_f.write(command.encode())
        self.isSensorOn = True

    def turn_sensor_off(self):
        command = 'off'
        self.ser_f.write(command.encode())
        self.isSensorOn = False

    def read_sensor(self, aquarium_type):
        retries = 5
        if self.isSensorOn:
            while retries > 0:
                try:
                    if self.ser_th is None:
                        self.connect()

                        if not self.isSensorOn:
                            self.turn_sensor_on()

                        self.ser_f.write(aquarium_type.encode())

                    line = self.ser_th.readline().decode("utf-8").split(",")

                    self.temperature = float(line[1])
                    self.humidity = float(line[2])
                    self.tapStatus = line[3]
                    self.fanStatus = line[4]

                    return (self.temperature, self.humidity, self.tapStatus, self.fanStatus)

                except RuntimeError as error:
                    print(error.args[0])
                    time.sleep(2.0)
                    retries -= 1

                except Exception as error:
                    self.disconnect()  # Close the port on any other exception
                    raise error

        return (self.temperature, self.humidity, self.tapStatus, self.fanStatus)
