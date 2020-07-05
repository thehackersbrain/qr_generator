# =======================================
# |	Author : Gaurav Raj [HackersBrain]	|
# |	Note : Give Credits before 			|
# |		  commiting any changes			|
# =======================================

import pyqrcode
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from os import getcwd

win = Tk()
win.title(" QR Code Generator | HackersBrain")
win.config(background="#4db8ff")


def generate():
    def sv():
        msg = messagebox.showinfo(title="Image Saved.",
                                  message=f"Image Saved Successfully !!!"
                                          f"\n\n{pt}/{file_name}.png")
        exit()
    pt = getcwd()
    text = entry1.get()
    qr = pyqrcode.create(text)
    file_name = "qrbyhackersbrain"
    name = file_name + '.png'

    qr.png(name, scale=10)
    image = Image.open(name)
    image = image.resize((400, 400), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    win.imagelabel.config(image=image)
    win.imagelabel.photo = image
    sav = ttk.Button(win, text="Save QR", command=sv)
    sav.grid(row=3, column=1, padx=3, pady=3)


text = ttk.Label(win, text="Enter text or Link : ")
text.grid(row=0, column=0, padx=3, pady=3)

entry1 = ttk.Entry(win, width=40)
entry1.grid(row=0, column=1, padx=3, pady=3)

button = ttk.Button(win, text="Generate", command=generate)
button.grid(row=1, column=1, padx=3, pady=3)

show_qr = ttk.Label(win, text=" QR Code : ")
show_qr.grid(row=1, column=0, padx=3, pady=3)

show_qr = ttk.Label(win, text=" HackersBrain ")
show_qr.grid(row=0, column=2, padx=3, pady=3)

win.imagelabel = ttk.Label(win, background="#6699ff")
win.imagelabel.grid(row=2, column=0, padx=3, pady=3, columnspan=3)

win.mainloop()
