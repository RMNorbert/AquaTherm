from gui.gui_theme_config import *

button_mode = True


# light-dark theme color switcher
def customize(aquarium_type_setter_input_box,
              sensor_controller_button,
              aquarium_type_setter_input,
              current_tap_image,
              current_fan_image,
              sensor_reading_box_image,
              dark_theme_controller_button,
              current_temperature_label,
              current_humidity_label,
              current_highest_temperature_label,
              current_status_label,
              current_fan_action_label,
              current_tap_action_label,
              sensor_reading_box_temperature_label,
              sensor_reading_box_humidity_label,
              sensor_reading_box_highest_temperature_label,
              root
              ):
    global button_mode

    if button_mode:
        aquarium_type_setter_input_box.config(bg=dark_theme_color)
        sensor_controller_button.config(bg=dark_theme_color, fg=light_theme_background_color)
        aquarium_type_setter_input.config(bg=dark_theme_background_color)
        current_tap_image.config(bg=dark_theme_color, activebackground=dark_theme_active_background_color)
        current_fan_image.config(bg=dark_theme_color, activebackground=dark_theme_active_background_color)
        sensor_reading_box_image.config(bg=dark_theme_color)
        dark_theme_controller_button.config(image=off, bg=dark_theme_color, activebackground=dark_theme_active_background_color)
        sensor_controller_button.config(bg=dark_theme_color, activebackground=dark_theme_active_background_color)
        current_temperature_label.config(bg=dark_theme_message_box_color)
        current_humidity_label.config(bg=dark_theme_message_box_color)
        current_highest_temperature_label.config(bg=dark_theme_message_box_color)
        current_status_label.config(bg=dark_theme_color, fg=dark_theme_status_color)
        current_fan_action_label.config(bg=dark_theme_color, fg=dark_theme_status_color)
        current_tap_action_label.config(bg=dark_theme_color, fg=dark_theme_status_color)
        sensor_reading_box_temperature_label.config(bg=dark_theme_message_box_color)
        sensor_reading_box_humidity_label.config(bg=dark_theme_message_box_color)
        sensor_reading_box_highest_temperature_label.config(bg=dark_theme_message_box_color)
        root.config(bg=dark_theme_color)
        button_mode = False
    else:
        aquarium_type_setter_input_box.config(bg=light_theme_background_color)
        sensor_controller_button.config(bg=sensor_controller_color,
                                        fg=dark_theme_background_color)
        aquarium_type_setter_input.config(bg=aquarium_type_input_color)
        sensor_reading_box_image.config(bg=light_theme_background_color)
        current_tap_image.config(bg=light_theme_background_color)
        current_fan_image.config(bg=light_theme_background_color)
        current_temperature_label.config(bg=light_theme_color)
        current_humidity_label.config(bg=light_theme_color)
        current_highest_temperature_label.config(bg=light_theme_color)
        current_status_label.config(bg=light_theme_background_color, fg=dark_theme_background_color)
        current_fan_action_label.config(bg=light_theme_background_color, fg=dark_theme_background_color)
        current_tap_action_label.config(bg=light_theme_background_color, fg=dark_theme_background_color)
        sensor_reading_box_temperature_label.config(bg=light_theme_color)
        sensor_reading_box_humidity_label.config(bg=light_theme_color)
        sensor_reading_box_highest_temperature_label.config(bg=light_theme_color)
        dark_theme_controller_button.config(image=on, bg=light_theme_background_color, activebackground=light_theme_background_color)
        sensor_controller_button.config(bg=light_theme_background_color, activebackground=light_theme_background_color)
        root.config(bg=light_theme_background_color)
        button_mode = True


def click(widget, *args):
    widget.delete(0, 'end')


# call function when leaving entry box
def leave(widget, *args):
    widget.focus()


