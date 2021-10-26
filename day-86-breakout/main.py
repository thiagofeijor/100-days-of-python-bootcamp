import time
from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
from block_manager import BlockManager

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

ball = Ball()
paddle = Paddle()
scoreboard = Scoreboard()
block = BlockManager()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")
block.start_game()

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()
    scoreboard.update_scoreboard()

    # Y
    if (ball.distance(paddle) < 50 and ball.ycor() < -270) or ball.ycor() > 260:
        ball.bounce_y()

    # X
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()

    # hit floor & restart game
    if ball.ycor() < -300:
        scoreboard.game_over()
        time.sleep(1)

        ball.start_game()
        block.start_game()

    # hit block
    for blck in block.all_blocks:
        if blck.distance(ball) < 50 and blck.isvisible():
            block.hit_block(blck)
            ball.bounce_y()

    # win game
    if block.hit_all():
        block.start_game()
        ball.increase_level()
        scoreboard.increase_level()


screen.exitonclick()
