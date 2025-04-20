import unittest
from src.game.paddle import Paddle

class TestPaddle(unittest.TestCase):
    def setUp(self):
        self.paddle = Paddle(x=50, y=100, width=10, height=60)

    def test_initial_position(self):
        self.assertEqual(self.paddle.x, 50)
        self.assertEqual(self.paddle.y, 100)

    def test_move_up(self):
        self.paddle.move(-10)
        self.assertEqual(self.paddle.y, 90)

    def test_move_down(self):
        self.paddle.move(10)
        self.assertEqual(self.paddle.y, 110)

    def test_boundary_conditions(self):
        self.paddle.move(-200)
        self.assertEqual(self.paddle.y, 0)  # Assuming the top boundary is 0
        self.paddle.move(200)
        self.assertEqual(self.paddle.y, 440)  # Assuming the bottom boundary is 500 - paddle height

if __name__ == '__main__':
    unittest.main()