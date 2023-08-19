from tkinter import *
import tkinter as tk
from sensor.arduino_multi_board_system_interface import *
# from sensor.arduino_one_board_system_interface import * # in case of one board

root = Tk()
root.title('AquaTherm')
root.geometry('900x600+300+200')
root.resizable(False, False)
root.config(bg='white')

light_theme_color = '#1ab5ef'
dark_theme_color = '#26242f'
dark_theme_message_box_color = '#17a2d7'
aquarium_type = 'cold'
button_mode = True
sensor_on = False


def scanning():
    if sensor_on:
        reading = read_sensor(aquarium_type)
        status = reading[2]
        temperature_c = str(reading[0])
        humidity = str(reading[1])
        highest_temp = str(get_highest_readings().temperature)

        t.config(text=temperature_c + '°C')
        h.config(text=humidity + '%')
        ht.config(text=highest_temp + '°C')
        s.config(text='Status: ' + status)
        update_fan_state(status)
        update_tap_state(status)
    # After 3 second, call scanning again (create a recursive loop)
    root.after(3000, scanning)


def switch_sensor():
    global sensor_on
    global aquarium_type

    if sensor_on:
        t.config(text='...')
        h.config(text='...')
        ht.config(text='...')
        s.config(text='')
        af.config(text='')
        at.config(text='')
        ti.config(image=remove)
        fi.config(image=remove)
        set_button.config(image=set_off)
        sensor_on = False
    else:
        if textfield.get() != '':
            aquarium_type = textfield.get()
        set_button.config(image=set_on)
        sensor_on = True


def customize():  # light-dark theme color switcher
    global button_mode

    if button_mode:
        myimage.config(bg=dark_theme_color)
        set_button.config(bg=dark_theme_color, fg='white')
        textfield.config(bg='black')
        ti.config(bg=dark_theme_color, activebackground='#26242f')
        fi.config(bg=dark_theme_color, activebackground='#26242f')
        box_myimage.config(bg=dark_theme_color)
        button.config(image=off, bg=dark_theme_color, activebackground='#26242f')
        set_button.config(bg=dark_theme_color, activebackground='#26242f')
        t.config(bg=dark_theme_message_box_color)
        h.config(bg=dark_theme_message_box_color)
        ht.config(bg=dark_theme_message_box_color)
        s.config(bg=dark_theme_color, fg='#ee666d')
        af.config(bg=dark_theme_color, fg='#ee666d')
        at.config(bg=dark_theme_color, fg='#ee666d')
        label1.config(bg=dark_theme_message_box_color)
        label2.config(bg=dark_theme_message_box_color)
        label3.config(bg=dark_theme_message_box_color)
        root.config(bg=dark_theme_color)
        button_mode = False
    else:
        myimage.config(bg='white')
        set_button.config(bg='lightgrey', fg='black')
        textfield.config(bg='#434343')
        box_myimage.config(bg='white')
        ti.config(bg='white')
        fi.config(bg='white')
        t.config(bg=light_theme_color)
        h.config(bg=light_theme_color)
        ht.config(bg=light_theme_color)
        s.config(bg='white', fg='black')
        af.config(bg='white', fg='black')
        at.config(bg='white', fg='black')
        label1.config(bg=light_theme_color)
        label2.config(bg=light_theme_color)
        label3.config(bg=light_theme_color)
        button.config(image=on, bg='white', activebackground='white')
        set_button.config(bg='white', activebackground='white')
        root.config(bg='white')
        button_mode = True


def click(*args):
    textfield.delete(0, 'end')


# call function when leaving entry box
def leave(*args):
    root.focus()


def update_fan_state(status):
    fan_status = control_fan(status)
    # fan = control_fan(reading[4]) # in case of one board
    af.config(text=fan_status)
    if 'on' in fan_status:
        fi.config(image=fan_on)
    else:
        fi.config(image=fan_off)


def update_tap_state(status):
    # tap = control_tap(reading[3]) # in case of one board
    tap_status = control_tap(status)
    at.config(text=tap_status)
    if 'on' in tap_status:
        ti.config(image=tap_on)
    else:
        ti.config(image=tap_off)


on = PhotoImage(file='images/light.png')
off = PhotoImage(file='images/dark.png')
set_off = PhotoImage(file='images/off.png')
set_on = PhotoImage(file='images/on.png')
tap_on = PhotoImage(file='images/tap-on.png')
tap_off = PhotoImage(file='images/tap-off.png')
fan_on = PhotoImage(file='images/fan-on.png')
fan_off = PhotoImage(file='images/fan-off.png')
remove = PhotoImage(file='images/remove.png')

button = Button(root,
                image=on,
                bd=0,
                bg='white',
                activebackground='white',
                highlightthickness=0,
                command=customize)

button.pack(padx=50, pady=50)
button.place(x=680)

Set_image = PhotoImage(file='images/set.png')
myimage = Label(image=Set_image)
myimage.place(x=10, y=10)
myimage.config(bg='white')


textfield = tk.Entry(root,
                     justify='center',
                     width=15,
                     font=('poppins', 22, 'bold'),
                     bd=0,
                     highlightthickness=0,
                     bg='#434343', fg='white')

textfield.insert(0, 'Set aquarium type')
textfield.place(x=43, y=23)
textfield.bind('<Button-1>', click)
textfield.bind('<Leave>', leave)


set_button = Button(image=set_off,
                    font=('poppins', 10, 'bold'),
                    cursor='hand2',
                    bd=0,
                    highlightthickness=0,
                    bg='white',
                    activebackground='white',
                    command=switch_sensor)

set_button.place(x=45, y=-6)
set_button.place(x=470)

Box_image = PhotoImage(file='images/box.png')
box_myimage = Label(image=Box_image)
box_myimage.config(bg='white')
box_myimage.pack(padx=5, pady=5, side=BOTTOM)

label1 = Label(root,
               text='Temperature',
               font=('Helvetica', 15, 'bold'),
               fg='white', bg=light_theme_color)

label2 = Label(root,
               text='Humidity',
               font=('Helvetica', 15, 'bold'),
               fg='white', bg=light_theme_color)

label3 = Label(root,
               text='Highest Temp',
               font=('Helvetica', 15, 'bold'),
               fg='white', bg=light_theme_color)

label1.place(x=125, y=500)
label2.place(x=330, y=500)
label3.place(x=530, y=500)

s = Label(font=('arial', 15, 'bold'), bg='white')
s.place(x=250, y=125)
fi = Label(bg='white')
fi.place(x=245, y=200)
ti = Label(bg='white')
ti.place(x=270, y=350)
af = Label(font=('arial', 15, 'bold'), bg='white')
af.place(x=350, y=250)
at = Label(font=('arial', 15, 'bold'), bg='white')
at.place(x=350, y=350)

t = Label(text='...', font=('arial', 25, 'bold'), bg=light_theme_color)
t.place(x=130, y=525)

h = Label(text='...', font=('arial', 25, 'bold'), bg=light_theme_color)
h.place(x=330, y=525)


ht = Label(text='...', font=('arial', 25, 'bold'), bg=light_theme_color)
ht.place(x=530, y=525)


root.after(3000, scanning)
root.mainloop()
