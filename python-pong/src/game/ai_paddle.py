from game.paddle import Paddle
from utils.constants import *

class AIPaddle(Paddle):
    def __init__(self, x, color):
        super().__init__(x, color)
        self.difficulty = 0.8  # AI reaction speed (0-1)
        
    def update(self, ball):
        # Predict ball position and move paddle
        if ball.dx > 0:  # Only move if ball is coming towards AI
            target_y = ball.y + ball.dy * ((self.x - ball.x) / ball.dx)
            target_y = max(0, min(target_y, WINDOW_HEIGHT - PADDLE_HEIGHT))
            
            # Add some imperfection to make it beatable
            if abs(self.y + PADDLE_HEIGHT/2 - target_y) > 10:
                if self.y + PADDLE_HEIGHT/2 < target_y:
                    self.move(up=False)
                else:
                    self.move(up=True)