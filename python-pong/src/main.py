import pygame
import sys
import time
import math
from game.paddle import Paddle
from game.ball import Ball
from game.menu import Menu
from game.ai_paddle import AIPaddle
from utils.constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, WHITE, BLUE, RED, GRAY, PADDLE_WIDTH
)

# Constants for font sizes
FONT_LARGE = 100
FONT_MEDIUM = 74
FONT_SMALL = 36

def draw_text(screen, text, size, x, y, color):
    """Draw text on the screen at a specified position."""
    font = pygame.font.Font(None, size)
    text_surface = font.render(str(text), True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def draw_center_line(screen):
    """Draw the center line with rounded dots."""
    for y in range(0, WINDOW_HEIGHT, 30):
        pygame.draw.circle(screen, GRAY, (WINDOW_WIDTH // 2, y), 5)

def draw_countdown(screen, number):
    """Draw a countdown with a pulsing effect."""
    screen.fill(BLACK)
    size = FONT_MEDIUM + int(abs(math.sin(time.time() * 5)) * 30)
    draw_text(screen, number, size, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, WHITE)
    pygame.display.flip()

def run_countdown(screen, clock):
    """Run a countdown before the game starts."""
    for i in range(3, 0, -1):
        start_time = time.time()
        while time.time() - start_time < 1:
            draw_countdown(screen, i)
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    draw_countdown(screen, "GO!")
    pygame.time.wait(1000)

def handle_paddle_movement(keys, left_paddle, right_paddle, game_mode, ball):
    """Handle paddle movement for both players."""
    if keys[pygame.K_w]:
        left_paddle.move(up=True)
    if keys[pygame.K_s]:
        left_paddle.move(up=False)

    if game_mode == "NORMAL MODE":
        if keys[pygame.K_UP]:
            right_paddle.move(up=True)
        if keys[pygame.K_DOWN]:
            right_paddle.move(up=False)
    else:  # AI MODE
        right_paddle.update(ball)

def main():
    """Main game loop."""
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()

    # Create menu
    menu = Menu(screen)
    game_mode = None

    # Menu loop
    while game_mode is None:
        menu.draw()
        pygame.display.flip()
        game_mode = menu.handle_input()
        clock.tick(60)
        if game_mode == "QUIT":
            pygame.quit()
            sys.exit()

    # Create game objects
    left_paddle = Paddle(50, BLUE)
    right_paddle = AIPaddle(WINDOW_WIDTH - 50 - PADDLE_WIDTH, RED) if game_mode == "AI MODE" else Paddle(WINDOW_WIDTH - 50 - PADDLE_WIDTH, RED)
    ball = Ball()

    # Score and game state
    score_left = 0
    score_right = 0
    paused = False

    # Countdown before starting
    run_countdown(screen, clock)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused

        if not paused:
            keys = pygame.key.get_pressed()
            handle_paddle_movement(keys, left_paddle, right_paddle, game_mode, ball)

            # Ball movement
            ball.move()

            # Ball collision with paddles
            if ball.rect.colliderect(left_paddle.rect):
                ball.dx = abs(ball.dx)  # Ensure ball moves right
                ball.increase_speed()
            elif ball.rect.colliderect(right_paddle.rect):
                ball.dx = -abs(ball.dx)  # Ensure ball moves left
                ball.increase_speed()

            # Score points and reset ball
            if ball.x <= 0:
                score_right += 1
                ball.reset()
            elif ball.x >= WINDOW_WIDTH:
                score_left += 1
                ball.reset()

        # Drawing
        screen.fill(BLACK)

        # Draw center line
        draw_center_line(screen)

        # Draw paddles, ball, and score
        left_paddle.draw(screen)
        right_paddle.draw(screen)
        ball.draw(screen)
        draw_text(screen, f"{score_left}", FONT_MEDIUM, WINDOW_WIDTH // 4, 50, BLUE)
        draw_text(screen, f"{score_right}", FONT_MEDIUM, 3 * WINDOW_WIDTH // 4, 50, RED)

        # Draw pause text
        if paused:
            draw_text(screen, "PAUSED", FONT_LARGE, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 2, (50, 50, 50))
            draw_text(screen, "PAUSED", FONT_LARGE, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, WHITE)
            draw_text(screen, "Press ESC to resume", FONT_SMALL, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50, GRAY)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
