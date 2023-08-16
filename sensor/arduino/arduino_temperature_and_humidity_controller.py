# to use pip install pyserial
import serial
import time
# 1st step : To set Arduino -> tools -> manage libraries -> search simple dht , install the package
# 2nd step : file -> samples -> select the sensor
# 3rd step: Use Arduino IDE to upload the firmware onto the arduino board
# with the current settings connect the sensor data wire to the second digital input
# the correct connection settings can be found in the arduino application -> tools -> port


class ArduinoTemperatureAndHumidityController:
    def __init__(self, port='COM5', baud_rate=115200):  # set the port and baud rate
        self.port = port
        self.baud_rate = baud_rate
        self.ser_th = None
        self.temperature = 0.0
        self.humidity = 0.0

    def connect(self):
        self.ser_th = serial.Serial(self.port, self.baud_rate, timeout=1)

    def disconnect(self):
        if self.ser_th is not None:
            self.ser_th.close()
            self.ser_th = None

    def switch_sensor(self, turn_off):
        retries = 5
        while retries > 0:
            try:
                if self.ser_th is None:
                    self.connect()

                line = self.ser_th.readline().decode("utf-8").split(",")

                if turn_off:
                    self.disconnect()

                self.temperature = float(line[1])
                self.humidity = float(line[2])

                return (self.temperature, self.humidity)

            except RuntimeError as error:
                print(error.args[0])
                time.sleep(2.0)
                retries -= 1

            except Exception as error:
                self.disconnect()  # Close the port on any other exception
                raise error

        return (self.temperature, self.humidity)