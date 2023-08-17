from sensor.status_analyzer import *
from database.db import *
from sensor.simulate.simulate_fan_controller import *
from sensor.simulate.simulate_tap_controller import *
from sensor.simulate.simulate_temperature_and_humidity_controller import *
from sensor.simulate.simulate_distance_controller import *
""" Use in case of sensors connected
from sensor.arduino.arduino_fan_controller import * # in case of arduino
from sensor.arduino.arduino_tap_controller import *
from sensor.arduino.arduino_temperature_and_humidity_controller import *

th_controller = ArduinoTemperatureAndHumidityController()
d_controller = ArduinoDistanceController()
f_controller = ArduinoFanController()
t_controller = ArduinoTapController()
"""
th_controller = TemperatureAndHumidityControllerSimulator()
d_controller = DistanceControllerSimulator()
f_controller = FanControllerSimulator()
t_controller = TapControllerSimulator()


def switch_temperature_and_humidity_sensor(command):
    if command == 'on':
        th_controller.connect()
    elif command == 'off':
        th_controller.disconnect()


def read_sensor(aquarium_type):
    reading = th_controller.read_sensor(aquarium_type)  # use this for simulated readings
    distance = d_controller.get_distance()
    # reading = th_controller.read_sensor() # use this in case of sensors connected
    temperature = reading[0]
    humidity = reading[1]
    status = get_status(temperature, humidity, aquarium_type, distance)
    store_readings(temperature, humidity, status)

    return (temperature, humidity, status)


def control_fan(status):
    if not f_controller.is_connected() and 'normal' not in status:
        if 'approaching upper limit temperature' in status:
            return f_controller.switch_fan('on with low speed')
        elif 'high temperature' in status:
            return f_controller.switch_fan('on with high speed')
        elif 'suboptimal' in status:
            return f_controller.switch_fan('on with low speed')

    elif 'normal' in status and f_controller.is_connected():
        return f_controller.switch_fan('off')
    else:
        return 'Fan: turned off'


def control_tap(status):
    if not t_controller.is_connected() and 'low water' in status:
        return t_controller.switch_tap('on')
    if t_controller.is_connected() and 'low water' not in status:
        return t_controller.switch_tap('off')
    else:
        return 'Tap: turned off'

