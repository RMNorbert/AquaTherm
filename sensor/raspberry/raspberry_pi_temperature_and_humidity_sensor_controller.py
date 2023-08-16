# pip3 install adafruit-circuitpython-dht
# sudo apt-get install libgpiod2
# imports for using a sensor to provide readings
import time
import board
import adafruit_dht

# 1 To be able to connect to the sensor write the Raspberry OS with Raspberry Pi Imager to an sd card
# 2 Insert the sd card to the board
# 3 A, Make a connection: with usb to the computer or connection can be made directly to mouse, keyboard, screen, speakers
# to the Raspberry board in this case the power needed for the board to turn on will be provided by the usb connection.
# 3 B, Finish the setup by starting the board (screen and at least a keyboard will be needed)
# during the setup the credentials for wifi connection can be set (if the board have a wireless connectivity)
# 3 C, After finishing the setup it is possible to just make a connection with the  ethernet cable or wifi.
# If only wifi connection or ethernet port used its important to provide a power outlet because raspberry pi does not have one initially.
# Initial the dht device, with data pin connected to:
# adafruit_dht.theTypeOfTheSensor(set here the board pin which the sensor is connected to)

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