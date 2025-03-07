from tkinter import *


window = Tk()
window.title("Converter")
window.minsize(300, 150)
window.config(padx=50, pady=30)


# Entry mile
mile_entry = Entry(width=7)
mile_entry.grid(row=1, column=2)


# Miles label
label_miles = Label(text="miles")
label_miles.grid(row=1, column=3)


# "is equal to" Label
label_equal = Label(text="is equal to")
label_equal.grid(row=2, column=1)


# km value
km_value = Label(text="0")
km_value.config(padx=20, pady=10)
km_value.grid(row=2, column=2)


# Kilometer Label
km_label = Label(text="km")
km_label.grid(row=2, column=3)


# Button Clicked Function
def button_clicked():
    mile_value = float(mile_entry.get())
    km = round((mile_value * 1.609344), 2)
    km_value.config(text=f"{km}")


# Calculate Button
calc_button = Button(text="Calculate", command=button_clicked)
calc_button.grid(row=3, column=2)


window.mainloop()