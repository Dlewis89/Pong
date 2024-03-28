from turtle import Screen
from actors.ball import Ball
from actors.paddle import Paddle
from actors.scoreboard import Scoreboard
import time

# Scren Setup
screen  = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

# Initialing Actors
l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball(0, 0)
scoreboard = Scoreboard()

# Screen Events
screen.listen()

# Left Paddle Controls
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Right Paddle Controls
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the Paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # Detects if left paddle scored
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset()

    # Detects if left paddle scored
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset()

# Closes the game
screen.exitonclick()