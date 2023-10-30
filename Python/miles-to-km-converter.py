import tkinter
from tkinter import *


def miles_to_km():
    miles_value = float(miles.get())
    ans = round(miles_value * 1.609)
    km.config(text=f"{ans}")


window = tkinter.Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

miles = tkinter.Entry()
miles.grid(column=2, row=0)

km = tkinter.Label(text=0)
km.grid(column=2, row=1)

# lable
converter = tkinter.Label(text="is equal to")
converter.grid(column=1, row=1)
#

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=3, row=0)

km_lable = tkinter.Label(text="Km")
km_lable.grid(column=3, row=1)

cal = tkinter.Button(text="Calculate",command=miles_to_km)
cal.grid(column=2, row=2)

window.mainloop()
