from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text="I am a label", font=("Arial", 20, "bold"))
my_label["text"] = "new_text"
my_label.config(text="new text")
my_label.grid(column=1, row=1)

# Button

def button_clicked():
    my_label.config(text="Text")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=2)

new_button = Button(text="New Button")
new_button.grid(row=1, column=3)

# Entry

input = Entry(width=10)
input.grid(column=4, row=3)





window.mainloop()