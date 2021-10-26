from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image
from PIL import ImageFont
import matplotlib.pyplot as plt
import os

YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

def makeWatermark():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.png*"),
                                                     ))
    label_file_explorer.configure(text="File Opened: " + filename)

    logo = Image.open('./tomato.png')
    image = Image.open(filename)

    image.paste(logo, (0, 0), logo)
    image.save('./final-file.png')

    image.show()

    messagebox.showinfo(title="Success", message="File saved!")


window = Tk()

window.title("Watermark logo")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Watermark logo", bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

label_file_explorer = Label(window, text="File Explorer using Tkinter", width=100, height=4, fg="blue")
label_file_explorer.grid(column=1, row=1)

button_explore = Button(window, text="Make Watermark", command=makeWatermark)
button_explore.grid(column=2, row=1)

window.mainloop()
