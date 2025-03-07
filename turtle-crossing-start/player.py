from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
NORTH = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -280)
        self.seth(NORTH)
        self.shape("turtle")
        self.color("fuchsia")


    def go_up(self):
        self.forward(10)

    def go_down(self):
        self.backward(10)


    def check_level_up(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(0, -280)
            return True
        else:
            return False