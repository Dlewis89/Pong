import time
from turtle import Screen
from actors.ball import Ball
from actors.paddle import Paddle
from actors.scoreboard import Scoreboard

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

# Meta data for the paddle
SCREEN_PADDLE_PADDING = 50
PADDLE_COLLISION_DISTANCE_THRESHOLD = 50
LEFT_PADDLE_SCORE_DISTANCE_THRESHOLD = RIGHT_SCREEN_BOUNDARY - 20
RIGHT_PADDLE_SCORE_DISTANCE_THRESHOLD = LEFT_SCREEN_BOUNDARY + 20
LEFT_PADDLE_UP_KEY = 'w'
LEFT_PADDLE_DOWN_KEY = 's'
RIGHT_PADDLE_UP_KEY = 'Up'
RIGHT_PADDLE_DOWN_KEY = 'Down'

# Meta data for the ball
BALL_COLLISION_DISTANCE_THRESHOLD = RIGHT_SCREEN_BOUNDARY - 80

# Initialing Actors
l_paddle = Paddle(LEFT_SCREEN_BOUNDARY + SCREEN_PADDLE_PADDING, 0)
r_paddle = Paddle(RIGHT_SCREEN_BOUNDARY - SCREEN_PADDLE_PADDING, 0)
ball = Ball()
scoreboard = Scoreboard()

# Screen Events
screen.listen()

# Left Paddle Controls
screen.onkey(l_paddle.go_up, LEFT_PADDLE_UP_KEY)
screen.onkey(l_paddle.go_down, LEFT_PADDLE_DOWN_KEY)

# Right Paddle Controls
screen.onkey(r_paddle.go_up, RIGHT_PADDLE_UP_KEY)
screen.onkey(r_paddle.go_down, RIGHT_PADDLE_DOWN_KEY)

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
    if ball.distance(r_paddle) < PADDLE_COLLISION_DISTANCE_THRESHOLD and ball.xcor() > BALL_COLLISION_DISTANCE_THRESHOLD or ball.distance(l_paddle) < PADDLE_COLLISION_DISTANCE_THRESHOLD and ball.xcor() < -BALL_COLLISION_DISTANCE_THRESHOLD:
        ball.bounce_x()
    
    # Detects if left paddle scored
    if ball.xcor() > LEFT_PADDLE_SCORE_DISTANCE_THRESHOLD:
        scoreboard.l_point()
        ball.reset()

    # Detects if right paddle scored
    if ball.xcor() < RIGHT_PADDLE_SCORE_DISTANCE_THRESHOLD:
        scoreboard.r_point()
        ball.reset()

# Closes the game
screen.exitonclick()