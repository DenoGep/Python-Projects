"""
Improvements to make:
    Count System
        Add a count system to the csv file (German, English, Count)
        When the user correctly knows the word make the count go up by 1
        After 3 or 4 counts remove the word from the words_to_learn.csv
        so the user can see a word at least 3 times because it's better for learning

    Mobility
        Add couple more languages and add everything as constants
        So you can change 3-4 lines max to switch languages
        (Maybe try to add an options section at the start of the program
        so the user can choose language)

    Difficulty
        After learning the most frequent 500 words
        the program should switch to 500 - 1000 frequency list and so on
        Maybe try to find a way so that with only 1 csv file you can quiz the first 500
        words and when it's done do the 500 - 1000 words automatically
"""

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = {}

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/german_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# Generate New Word Function
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfigure(card_title, text="German", fill="black")
    canvas.itemconfigure(card_word, text=current_card["German"], fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_word, fill="white", text=current_card["English"])
    canvas.itemconfig(card_title, fill=BACKGROUND_COLOR, text="English")


flip_timer = window.after(3000, func=flip_card)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)

card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=1, column=1, columnspan=2)

# Right Button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=2, column=2)

# Wrong Button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=2, column=1)

next_card()

window.mainloop()