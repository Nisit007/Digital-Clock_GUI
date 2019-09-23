import sys
from tkinter import *
import tkinter
import time

window = tkinter.Tk()
window.geometry("1250x500")
window.title("Digital Clock")


def times():
    named_tuple = time.localtime()
    current_time = time.strftime("%H:%M:%S \n %d:%m:%Y", named_tuple)
    clock.config(text=current_time)
    clock.after(200, times)


clock = Label(window, font=("times", 45, "bold"), bg="black", fg="yellow")
clock.place(x=420, y=150)
times()

digi = Label(window, text="Digital Clock", font=("times 35 bold"))
digi.place(x=430, y=60)


label1 = Label(window, text="@Develop By Nisitpatel", font=("italic 23 bold"))
label1.place(x=370, y=400)
window.mainloop()
