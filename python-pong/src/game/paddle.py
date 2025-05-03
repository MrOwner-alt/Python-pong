import pygame
from utils.constants import *

class Paddle:
    def __init__(self, x, color):
        self.x = x
        self.y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
        self.color = color
        self.rect = pygame.Rect(x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT)
        
    def move(self, up=True):
        """Move the paddle up or down."""
        if up and self.y > 0:
            self.y -= PADDLE_SPEED
        if not up and self.y < WINDOW_HEIGHT - PADDLE_HEIGHT:
            self.y += PADDLE_SPEED
        self.rect.y = self.y
        
    def draw(self, screen):
        """Draw the paddle with a gradient effect."""
        # Draw the outer rectangle (main paddle color)
        pygame.draw.rect(screen, self.color, self.rect)
        
        # Draw the inner rectangle (lighter gradient effect)
        inner_rect = pygame.Rect(self.x + 3, self.y + 3, PADDLE_WIDTH - 6, PADDLE_HEIGHT - 6)
        lighter_color = (
            min(255, self.color[0] + 50),  # Increase red component
            min(255, self.color[1] + 50),  # Increase green component
            min(255, self.color[2] + 50)   # Increase blue component
        )
        pygame.draw.rect(screen, lighter_color, inner_rect)
