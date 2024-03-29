import unittest
from actors.ball import Ball

class TestBallMethods(unittest.TestCase):

    def setUp(self):
        self.ball = Ball(10, 10)

    def test_ball_move(self):
        ball_x = self.ball.xcor()
        ball_y = self.ball.ycor()

        self.ball.move()

        self.assertEqual(self.ball.xcor(), ball_x + self.ball.x_move)
        self.assertEqual(self.ball.ycor(), ball_y + self.ball.y_move)
    
    def test_ball_bounce_x(self):

        ball_x_move = self.ball.x_move

        self.ball.bounce_x()

        self.assertEqual(self.ball.x_move, -ball_x_move)

    def test_ball_bounce_y(self):
        ball_y_move = self.ball.y_move

        self.ball.bounce_y()

        self.assertEqual(self.ball.y_move, -ball_y_move)

    def test_ball_reset(self):

        ball_x = self.ball.xcor()
        ball_y = self.ball.ycor()

        self.ball.reset()

        self.assertEqual(self.ball.xcor(), 0)
        self.assertEqual(self.ball.ycor(), 0)
        self.assertEqual(round(self.ball.move_speed, 2), 0.09)

if __name__ == '__main__':
    unittest.main()