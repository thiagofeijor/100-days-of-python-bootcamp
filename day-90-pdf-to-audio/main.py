from tkinter import *
from tkinter import filedialog, messagebox
from boto3 import client
import fitz

YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

def convert():
    filename = filedialog.askopenfilename(title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.pdf*"),
                                                     ))
    label_file_explorer.configure(text="File Opened: " + filename)

    text = ""
    with fitz.open(filename) as doc:
        for page in doc:
            text += page.getText()

    print(f"Text: {text}")
    polly = client('polly', region_name='us-west-2')

    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='file_convert')

    stream = response.get('AudioStream')

    with open('output_aws_polly.mp3', 'wb') as f:
        data = stream.read()
        f.write(data)

    messagebox.showinfo(title="Success", message="File saved!")


window = Tk()

window.title("PDF to Audio")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="PDF to Audio", bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

label_file_explorer = Label(window, text="File Explorer using Tkinter", width=100, height=4, fg="blue")
label_file_explorer.grid(column=1, row=1)

button_explore = Button(window, text="Convert", command=convert)
button_explore.grid(column=2, row=1)

window.mainloop()
