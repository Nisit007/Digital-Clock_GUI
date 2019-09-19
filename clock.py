import sys
from tkinter import *
import tkinter
import time

window = tkinter.Tk()
window.geometry("1250x500")
window.title("Digital Clock")


def times():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200, times)


clock = Label(window, font=("times", 50, "bold"), bg="black", fg="yellow")
clock.place(x=420, y=160)
times()

digi = Label(window, text="Digital Clock", font=("times 24 bold"))
digi.place(x=450, y=110)

digi1 = Label(window, text="Hours     Minutes     Seconds", font=("times 16 bold"))
digi1.place(x=425, y=250)

label1 = Label(window, text="@Develop By Nisitpatel", font=("italic 23 bold"))
label1.place(x=370, y=400)
window.mainloop()
