import turtle
import pandas #22gun
FONT = ("Times New Roman", 10, "normal")

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []
correct_answer = 0
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{correct_answer}/50 States Correct",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states and answer_state not in guessed_states:
        correct_answer += 1
        guessed_states.append(answer_state)

        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)