from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")

    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# -------------------------- SEARCH PASSWORD -------------------------- #

def find_password():
    website = website_entry.get().lower()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if len(website) == 0:
            messagebox.showwarning(title="Oops", message="Please don't leave the website field empty!")

        else:
            lower_dict = {k.lower(): v for k, v in data.items()}
            if website in lower_dict:
                password = lower_dict[website]["password"]
                email = lower_dict[website]["email"]
                messagebox.showinfo(title=website, message=f"Email: {email}\n"
                                                           f"Password: {password}")
            else:
                messagebox.showwarning(title="Warning", message=f"No details for {website_entry.get()} found.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(550, 400)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=1, column=1, columnspan=3)

# Website Label
website_label = Label(text="Website:")
website_label.grid(row=2, column=1)

# Email/Username Label
email_label = Label(text="Email / Username:")
email_label.grid(row=3, column=1)

# Password Label
password_label = Label(text="Password:")
password_label.grid(row=4, column=1)

# Website Entry
website_entry = Entry(width=21)
website_entry.grid(row=2, column=2)
website_entry.focus()

# Search Button
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=2, column=3)

# Email / Username Entry
email_entry = Entry(width=38)
email_entry.grid(row=3, column=2, columnspan=2)
email_entry.insert(0, "dodogep@gmail.com")

# Password Entry
password_entry = Entry(width=21)
password_entry.grid(row=4, column=2)

# Generate Password Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=3)

# Add Button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=5, column=2, columnspan=2)

window.mainloop()
