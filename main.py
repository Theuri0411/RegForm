from tkinter import *
from tkinter.font import Font
root = Tk()
root.geometry("500x300")

Label(root, text="REGISTRATION FORM", font="ar 15 bold").grid(row=0, column=3)

name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
payment_mode = Label(root, text="Payment Mode")

name.grid(row=, column=2)


root.mainloop()
