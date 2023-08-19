# imports for using a sensor to provide readings
import time
import board
import adafruit_dht

"""
 you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
 This may be necessary on a Linux single board computer like the Raspberry Pi,
 but it will not work in CircuitPython.
"""


class DHTSensor:
    def __init__(self, pin=board.D18):
        self.dhtDevice = adafruit_dht.DHT22(pin)  # DHT22 (or an AM2302) sensor connected to Pin 4,
        self.temperature_c = 0.0
        self.temperature_f = 0.0
        self.humidity = 0.0

    def operate(self):
        retries = 5
        while retries > 0:
            try:
                # Print the values to the serial port
                self.temperature_c = self.dhtDevice.temperature
                self.temperature_f = self.temperature_c * (9 / 5) + 32
                self.humidity = self.dhtDevice.humidity
                print(
                    "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                        self.temperature_f, self.temperature_c, self.humidity
                    )
                )
                return (self.temperature_c, self.humidity)

            except RuntimeError as error:
                # Errors happen fairly often, DHT's are hard to read, just keep going
                print(error.args[0])
                time.sleep(2.0)
                retries -= 1

            except Exception as error:
                self.dhtDevice.exit()
                raise error

        return (self.temperature_c, self.humidity)