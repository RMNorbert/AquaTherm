from gui.gui_functions import *


aquarium_type_setter_input_box = Label(image=aquarium_type_setter_image)
aquarium_type_setter_input_box.place(x=aquarium_type_setter_input_box_position, y=aquarium_type_setter_input_box_position)
aquarium_type_setter_input_box.config(bg=light_theme_background_color)

aquarium_type_setter_input = tk.Entry(root, justify=center_placed, width=basic_font_size,
                                      font=(input_font_style, aquarium_type_setter_input_font_size, bold_font_style),
                                      bd=zero_to_hide_attribute, highlightthickness=zero_to_hide_attribute,
                                      bg=aquarium_type_input_color, fg=light_theme_background_color)

aquarium_type_setter_input.insert(0, aquarium_type_setter_input_text)
aquarium_type_setter_input.place(x=aquarium_type_setter_input_x_position, y=aquarium_type_setter_input_y_position)


sensor_controller_button = Button(image=set_off,
                                  cursor=sensor_controller_button_cursor_type,
                                  bd=zero_to_hide_attribute, highlightthickness=zero_to_hide_attribute,
                                  bg=light_theme_background_color, activebackground=light_theme_background_color)

sensor_controller_button.place(x=sensor_controller_button_x_position, y=sensor_controller_button_y_position)

sensor_reading_box_image = Label(image=sensor_reading_box_image)
sensor_reading_box_image.config(bg=light_theme_background_color)
sensor_reading_box_image.pack(padx=sensor_reading_box_image_padding, pady=sensor_reading_box_image_padding, side=BOTTOM)

sensor_reading_box_temperature_label = Label(root,
                                             text=temperature_label_text,
                                             font=(sensor_reading_label_font_style, basic_font_size, bold_font_style),
                                             fg=light_theme_background_color, bg=light_theme_color)

sensor_reading_box_humidity_label = Label(root,
                                          text=humidity_label_text,
                                          font=(sensor_reading_label_font_style, basic_font_size, bold_font_style),
                                          fg=light_theme_background_color, bg=light_theme_color)

sensor_reading_box_highest_temperature_label = Label(root,
                                                     text=highest_temperature_label_text,
                                                     font=(sensor_reading_label_font_style, basic_font_size, bold_font_style),
                                                     fg=light_theme_background_color, bg=light_theme_color)

sensor_reading_box_temperature_label.place(x=sensor_reading_box_temperature_label_x_position, y=sensor_reading_box_label_y_position)
sensor_reading_box_humidity_label.place(x=sensor_reading_box_humidity_label_x_position, y=sensor_reading_box_label_y_position)
sensor_reading_box_highest_temperature_label.place(x=sensor_reading_box_highest_temperature_label_x_position, y=sensor_reading_box_label_y_position)

current_status_label = Label(font=(reading_font_style, basic_font_size, bold_font_style),
                             bg=light_theme_background_color)
current_status_label.place(x=current_status_label_x_position, y=current_status_label_y_position)

current_fan_image = Label(bg=light_theme_background_color)
current_fan_image.place(x=current_fan_image_x_position, y=current_fan_image_y_position)

current_tap_image = Label(bg=light_theme_background_color)
current_tap_image.place(x=current_tap_image_x_position, y=current_tap_image_y_position)

current_fan_action_label = Label(font=(reading_font_style, basic_font_size, bold_font_style),
                                 bg=light_theme_background_color)
current_fan_action_label.place(x=current_action_label_x_position, y=current_fan_action_label_y_position)

current_tap_action_label = Label(font=(reading_font_style, basic_font_size, bold_font_style),
                                 bg=light_theme_background_color)
current_tap_action_label.place(x=current_action_label_x_position, y=current_tap_action_label_y_position)

current_temperature_label = Label(text=empty_reading_text,
                                  font=(reading_font_style, reading_font_size, bold_font_style),
                                  bg=light_theme_color)
current_temperature_label.place(x=current_temperature_label_x_position, y=current_label_y_position)

current_humidity_label = Label(text=empty_reading_text,
                               font=(reading_font_style, reading_font_size, bold_font_style),
                               bg=light_theme_color)
current_humidity_label.place(x=current_humidity_label_x_position, y=current_label_y_position)


current_highest_temperature_label = Label(text=empty_reading_text,
                                          font=(reading_font_style, reading_font_size, bold_font_style),
                                          bg=light_theme_color)
current_highest_temperature_label.place(x=current_highest_temperature_label_x_position, y=current_label_y_position)

dark_theme_controller_button = Button(root, image=on, bd=zero_to_hide_attribute,
                                      bg=light_theme_background_color, activebackground=light_theme_background_color,
                                      highlightthickness=zero_to_hide_attribute)

dark_theme_controller_button.pack(padx=theme_controller_button_padding,
                                  pady=theme_controller_button_padding)
dark_theme_controller_button.place(x=theme_controller_button_x_position)

dark_theme_controller_button.config(command=lambda: customize(
                                    aquarium_type_setter_input_box, sensor_controller_button,
                                    aquarium_type_setter_input, current_tap_image, current_fan_image,
                                    sensor_reading_box_image, dark_theme_controller_button, current_temperature_label,
                                    current_humidity_label, current_highest_temperature_label, current_status_label,
                                    current_fan_action_label, current_tap_action_label,
                                    sensor_reading_box_temperature_label, sensor_reading_box_humidity_label,
                                    sensor_reading_box_highest_temperature_label, root)
                                    )

aquarium_type_setter_input.bind('<Button-1>', lambda event: click(aquarium_type_setter_input))
aquarium_type_setter_input.bind('<Leave>', lambda event: leave(root))
