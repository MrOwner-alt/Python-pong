import unittest
from src.game.ball import Ball

class TestBall(unittest.TestCase):
    def setUp(self):
        self.ball = Ball()

    def test_initial_position(self):
        self.assertEqual(self.ball.x, 0)
        self.assertEqual(self.ball.y, 0)

    def test_move(self):
        self.ball.move()
        self.assertNotEqual(self.ball.x, 0)
        self.assertNotEqual(self.ball.y, 0)

    def test_reset(self):
        self.ball.move()
        self.ball.reset()
        self.assertEqual(self.ball.x, 0)
        self.assertEqual(self.ball.y, 0)

if __name__ == '__main__':
    unittest.main()