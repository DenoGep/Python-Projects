from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
GREEN = "#65B741"
RED = "#FE0000"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        # Question Card
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=250,
                                                     text="question here",
                                                     font=FONT, fill="black")
        self.canvas.grid(row=2, column=1, columnspan=2, pady=40, padx=20)
        # True Button
        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, padx=20, pady=20, command=self.true_pressed)
        self.true_button.grid(row=3, column=1)
        # False Button
        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, padx=20, pady=20, command=self.false_pressed)
        self.false_button.grid(row=3, column=2)
        # Scoreboard
        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", padx=20, pady=20,
                                 font=("Arial", 17, "normal"))
        self.score_label.grid(row=1, column=2)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)
        self.window.after(1000, self.get_next_question)