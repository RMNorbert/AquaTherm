from gui.gui_config import *
from sensor.arduino_multi_board_system_interface import *
# from sensor.arduino_one_board_system_interface import * # in case of one board
aquarium_type = 'cold'
sensor_on = False


def scanning():
    if sensor_on:
        reading = read_sensor(aquarium_type)
        current_status = reading[2]
        current_temperature_in_c = str(reading[0])
        current_humidity = str(reading[1])
        current_highest_temp = str(get_highest_readings().temperature)

        current_temperature_label.config(text=current_temperature_in_c + '°C')
        current_humidity_label.config(text=current_humidity + '%')
        current_highest_temperature_label.config(text=current_highest_temp + '°C')
        current_status_label.config(text='Status: ' + current_status)
        update_fan_state(current_status)
        update_tap_state(current_status)
    # After 3 second, call scanning again (create a recursive loop)
    root.after(three_second_delay, scanning)


def update_fan_state(status):
    fan_status = control_fan(status)
    # fan = control_fan(reading[4]) # in case of one board
    current_fan_action_label.config(text=fan_status)
    if 'on' in fan_status:
        current_fan_image.config(image=fan_on)
    else:
        current_fan_image.config(image=fan_off)


def update_tap_state(status):
    # tap = control_tap(reading[3]) # in case of one board
    tap_status = control_tap(status)
    current_tap_action_label.config(text=tap_status)
    if 'on' in tap_status:
        current_tap_image.config(image=tap_on)
    else:
        current_tap_image.config(image=tap_off)


def switch_sensor():
    global sensor_on
    global aquarium_type

    if sensor_on:
        current_temperature_label.config(text=empty_reading_text)
        current_humidity_label.config(text=empty_reading_text)
        current_highest_temperature_label.config(text=empty_reading_text)
        current_status_label.config(text=blank_text)
        current_fan_action_label.config(text=blank_text)
        current_tap_action_label.config(text=blank_text)
        current_tap_image.config(image=remove)
        current_fan_image.config(image=remove)
        sensor_controller_button.config(image=set_off)
        sensor_on = False
    else:
        if aquarium_type_setter_input.get() != blank_text:
            aquarium_type = aquarium_type_setter_input.get()
        sensor_controller_button.config(image=set_on)
        sensor_on = True


sensor_controller_button.config(command=switch_sensor)

root.after(three_second_delay, scanning)
root.mainloop()
