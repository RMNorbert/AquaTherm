from tkinter import *
import tkinter as tk
# window style settings
root = Tk()
root.title('AquaTherm')
root.geometry('900x600+300+200')
root.resizable(False, False)
root.config(bg='white')

three_second_delay = 3000

# used images
on = PhotoImage(file='./images/light.png')
off = PhotoImage(file='./images/dark.png')
set_off = PhotoImage(file='./images/off.png')
set_on = PhotoImage(file='./images/on.png')
tap_on = PhotoImage(file='./images/tap-on.png')
tap_off = PhotoImage(file='./images/tap-off.png')
fan_on = PhotoImage(file='./images/fan-on.png')
fan_off = PhotoImage(file='./images/fan-off.png')
remove = PhotoImage(file='./images/remove.png')
aquarium_type_setter_image = PhotoImage(file='./images/set.png')
sensor_reading_box_image = PhotoImage(file='./images/box.png')

# color related settings
light_theme_color = '#1ab5ef'
light_theme_background_color = 'white'
dark_theme_color = '#26242f'
dark_theme_status_color = '#ee666d'
dark_theme_background_color = 'black'
dark_theme_active_background_color = '#26242f'
dark_theme_message_box_color = '#17a2d7'
sensor_controller_color = 'lightgrey'
aquarium_type_input_color = '#434343'

# element attribute related settings
center_placed = 'center'
zero_to_hide_attribute = 0
sensor_controller_button_cursor_type = 'hand2'

# element placings
theme_controller_button_padding = 50
theme_controller_button_x_position = 680

aquarium_type_setter_input_box_position = 10
aquarium_type_setter_input_x_position = 43
aquarium_type_setter_input_y_position = 23

sensor_controller_button_x_position = 470
sensor_controller_button_y_position = -6

sensor_reading_box_image_padding = 5
sensor_reading_box_label_y_position = 500
sensor_reading_box_temperature_label_x_position = 125
sensor_reading_box_humidity_label_x_position = 330
sensor_reading_box_highest_temperature_label_x_position = 530

current_status_label_x_position = 250
current_status_label_y_position = 125

current_action_label_x_position = 350
current_fan_image_x_position = 245
current_fan_image_y_position = 200
current_fan_action_label_y_position = 250

current_tap_image_x_position = 270
current_tap_image_y_position = 350
current_tap_action_label_y_position = 350

current_label_y_position = 525
current_temperature_label_x_position = 130
current_humidity_label_x_position = 330
current_highest_temperature_label_x_position = 530
# text related settings
reading_font_size = 25
aquarium_type_setter_input_font_size = 22
basic_font_size = 15

reading_font_style = 'arial'
sensor_reading_label_font_style = 'Helvetica'
input_font_style = 'poppins'
bold_font_style = 'bold'

aquarium_type_setter_input_text = 'Set aquarium type'
temperature_label_text = 'Temperature'
highest_temperature_label_text = 'Highest Temp'
humidity_label_text = 'Humidity'
empty_reading_text = '...'
blank_text = ''
