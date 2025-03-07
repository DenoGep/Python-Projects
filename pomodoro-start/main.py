from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
TITLE_COLOR = "#A0C49D"  #"#9bdeac"
BG_COLOR = "#e1ecc8" #"#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        count_down(work_sec)
        title_label.config(text="Work", fg=TITLE_COLOR)
    elif reps == 8:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    else:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BG_COLOR)

canvas = Canvas(width=250, height=250, bg=BG_COLOR, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(125, 125, image=tomato_img)
timer_text = canvas.create_text(125, 145, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)


# Timer Label
title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=BG_COLOR, fg=TITLE_COLOR)
title_label.grid(row=1, column=2)


# Start button
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=3, column=1)


# Reset button
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=3, column=3)


# Check mark Label
check_mark = Label(bg=BG_COLOR, fg=TITLE_COLOR)
check_mark.grid(row=4, column=2)


window.mainloop()