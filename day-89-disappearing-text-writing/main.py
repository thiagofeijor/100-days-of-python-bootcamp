import math
from tkinter import *
import datetime
import math

last_time = ''
timer = None

def get_diff():
    global last_time
    if not last_time:
        return 0

    current_time = (datetime.datetime.now() - last_time).total_seconds()
    return math.floor(current_time)

def get_label():
    return f"Disappearing in: {10 - get_diff()}"

def count_down():
    global last_time
    global timer

    if timer:
        window.after_cancel(timer)

    if get_diff() > 9:
        text.delete(0, 'end')
        last_time = datetime.datetime.now()
    else:
        timer = window.after(1000, count_down)

    title_label.config(text=get_label())


def on_key_press(_):
    global last_time
    last_time = datetime.datetime.now()
    count_down()

window = Tk()

window.title("Disappearing Text Writing")
window.config(padx=100, pady=50)

title_label = Label(text=get_label())
title_label.grid(column=1, row=0)

text = Entry(window)
text.grid(column=1, row=1)
text.focus()

window.bind('<KeyPress>', on_key_press)
window.mainloop()