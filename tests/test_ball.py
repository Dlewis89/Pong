import unittest
from actors.ball import Ball

class TestBallMethods(unittest.TestCase):

    def setUp(self):
        self.ball = Ball()

    def test_ball_move(self):
        self.ball.move()

        self.assertEqual(self.ball.xcor(), 10)
        self.assertEqual(self.ball.ycor(), 10)
    
    def test_ball_bounce_x(self):
        self.ball.bounce_x()

        self.assertEqual(self.ball.x_move, -10)

    def test_ball_bounce_y(self):
        self.ball.bounce_y()

        self.assertEqual(self.ball.y_move, -10)

    def test_ball_reset(self):
        self.ball.reset()

        self.assertEqual(self.ball.xcor(), 0)
        self.assertEqual(self.ball.ycor(), 0)
        self.assertEqual(round(self.ball.move_speed, 2), 0.09)

if __name__ == '__main__':
    unittest.main()