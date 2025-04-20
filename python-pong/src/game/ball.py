import pygame
import random
import math
from utils.constants import *

class Ball:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT // 2
        self.speed = INITIAL_BALL_SPEED
        
        # More challenging initial angles
        angles = [
            random.uniform(math.pi/6, math.pi/3),    # Up-right
            random.uniform(-math.pi/3, -math.pi/6),  # Down-right
            random.uniform(2*math.pi/3, 5*math.pi/6),# Up-left
            random.uniform(-5*math.pi/6, -2*math.pi/3)# Down-left
        ]
        
        # Randomly choose one of the four diagonal directions
        angle = random.choice(angles)
        
        # Add slight randomness to speed
        self.speed += random.uniform(-0.5, 1.0)
        
        self.dx = self.speed * math.cos(angle)
        self.dy = self.speed * math.sin(angle)
        self.rect = pygame.Rect(self.x, self.y, BALL_SIZE, BALL_SIZE)
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        
        # Wall collision
        if self.y <= 0 or self.y >= WINDOW_HEIGHT - BALL_SIZE:
            self.dy *= -1
            
        self.rect.x = self.x
        self.rect.y = self.y
        
    def increase_speed(self):
        current_angle = math.atan2(self.dy, self.dx)
        self.speed += BALL_ACCELERATION
        
        # Add slight randomness to the bounce angle
        angle_variation = random.uniform(-0.2, 0.2)
        new_angle = current_angle + angle_variation
        
        # Ensure the ball doesn't move too vertically
        if abs(math.sin(new_angle)) > 0.9:
            new_angle = current_angle
            
        self.dx = self.speed * math.cos(new_angle)
        self.dy = self.speed * math.sin(new_angle)
        
    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x + BALL_SIZE/2), int(self.y + BALL_SIZE/2)), BALL_SIZE//2)