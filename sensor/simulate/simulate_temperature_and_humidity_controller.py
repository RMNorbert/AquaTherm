import random
import time


class TemperatureAndHumidityControllerSimulator:
    def __init__(self):
        self.ser_th = None

    def connect(self):
        self.ser_th = True

    def disconnect(self):
        if self.ser_th is not None:
            self.ser_th = None

    def read_sensor(self, aquarium_type):
        retries = 5
        while retries > 0:
            try:
                if self.ser_th is None:
                    self.connect()

                temperature = None
                humidity = None

                if aquarium_type == "cold":
                    temperature = round(random.uniform(10.0, 24.0), 2)
                    humidity = round(random.uniform(35.0, 80.0), 2)

                elif aquarium_type == "tropical":
                    temperature = round(random.uniform(21.0, 32.0), 2)
                    humidity = round(random.uniform(60.0, 80.0), 2)

                else:
                    temperature = round(random.uniform(21.0, 27.5), 2)
                    humidity = round(random.uniform(60, 85), 2)

                return (temperature, humidity)

            except RuntimeError as error:
                print(error.args[0])
                time.sleep(2.0)
                retries -= 1

            except Exception as error:
                self.disconnect()  # Close the port on any other exception
                raise error

        return (None, None)