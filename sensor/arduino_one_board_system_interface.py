from sensor.status_analyzer import *
from database.db import *
from sensor.arduino.arduino_sensor_controller import *

sensor_controller = ArduinoSensorController()


def switch_connection_to_sensors(command):
    if command == 'on':
        sensor_controller.connect()
    elif command == 'off':
        sensor_controller.disconnect()


def switch_sensor(command):
    if command == 'on':
        sensor_controller.turn_sensor_on()
    elif command == 'off':
        sensor_controller.turn_sensor_off()


def read_sensor(aquarium_type):
    reading = sensor_controller.read_sensor(aquarium_type)

    temperature = reading[0]
    humidity = reading[1]
    tap_status = reading[2]
    fan_status = reading[3]
    status = get_status(temperature, humidity, aquarium_type)

    store_readings(temperature, humidity, status)

    return (temperature, humidity, status, tap_status, fan_status)

