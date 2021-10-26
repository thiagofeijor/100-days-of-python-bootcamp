from turtle import Turtle

Y_INDEX = -280
class Paddle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, Y_INDEX)

    def go_left(self):
        if self.xcor() < Y_INDEX:
            return

        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        if self.xcor() > (Y_INDEX * -1):
            return

        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
