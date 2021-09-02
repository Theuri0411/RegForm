from tkinter import *
from tkinter.font import Font
root = Tk()
root.geometry("500x300")

Label(root, text="PY REGISTRATION FORM",
      font="ar 15 bold").grid(row=0, column=3)

name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
payment_mode = Label(root, text="Payment Mode")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
payment_mode.grid(row=5, column=2)

name_value = StringVar
phone_value = StringVar
gender_value = StringVar
emergency_value = StringVar
payment_value = StringVar
check_value = IntVar


name_entry = Entry(root, textvariable=name_value)
phone_entry = Entry(root, textvariable=phone_value)
gender_entry = Entry(root, textvariable=gender_value)
emerency_entry = Entry(root, textvariable=emergency_value)
payment_entry = Entry(root, textvariable=payment_value)


root.mainloop()
