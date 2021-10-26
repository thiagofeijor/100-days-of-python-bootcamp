from tkinter import *
import datetime

last_time = ''
time_list = []

def total_time():
    total_seconds = sum(time_list) / (len(time_list) or 1)
    total_time = datetime.timedelta(seconds=total_seconds)
    return f"Typing Speed: {total_time}"

def onKeyPress(event):
    global last_time
    current_time = datetime.datetime.now()

    if last_time:
        difference = (current_time - last_time).total_seconds()
        time_list.append(difference)

    last_time = current_time
    text.insert('end', f"{event.char}")
    title_label.config(text=total_time())

window = Tk()

window.title("Typing Speed")
window.config(padx=100, pady=50)

title_label = Label(text=total_time())
title_label.grid(column=1, row=0)

text = Entry(window)
text.grid(column=1, row=1)

window.bind('<KeyPress>', onKeyPress)
window.mainloop()