from turtle import Screen
from actors.ball import Ball
from actors.paddle import Paddle
from actors.scoreboard import Scoreboard
import time

# Screen Setup
screen  = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

# Get the screen boundaries based on turtle coordinate system
TOP_SCREEN_BOUNDARY = screen.window_height() // 2 * -1 
LEFT_SCREEN_BOUNDARY = screen.window_width() // 2 * -1
RIGHT_SCREEN_BOUNDARY = screen.window_width() // 2
BOTTOM_SCREEN_BOUNDARY = screen.window_height() // 2

SCREEN_PADDLE_PADDING = 50


# Initialing Actors
l_paddle = Paddle(LEFT_SCREEN_BOUNDARY + SCREEN_PADDLE_PADDING, 0)
r_paddle = Paddle(RIGHT_SCREEN_BOUNDARY - SCREEN_PADDLE_PADDING, 0)
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
    if ball.ycor() > BOTTOM_SCREEN_BOUNDARY - ball.pensize() or ball.ycor() < TOP_SCREEN_BOUNDARY + ball.pensize():
        ball.bounce_y()

    # Detect collision with the Paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # Detects if left paddle scored
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset()

    # Detects if right paddle scored
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset()

# Closes the game
screen.exitonclick()