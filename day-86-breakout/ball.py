from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.start_game()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def increase_level(self):
        self.reset_position()
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, -200)
        self.x_move = 3
        self.y_move = 3

    def start_game(self):
        self.move_speed = 2
        self.reset_position()
