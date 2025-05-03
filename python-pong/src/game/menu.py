import pygame
import math
import time

# Game constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
GRAY = (200, 200, 200)

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.selected_option = 0
        self.options = ["NORMAL MODE", "AI MODE", "HOW TO PLAY", "QUIT"]
        self.showing_controls = False

    def draw(self):
        self.screen.fill(BLACK)

        if self.showing_controls:
            self._draw_controls()
        else:
            self._draw_menu()

    def _draw_menu(self):
        title_size = 100
        option_size = 50

        # Draw title with pulsing effect and gradient
        pulse = abs(math.sin(time.time() * 2)) * 20
        title_size = int(title_size + pulse)
        font = pygame.font.Font(None, title_size)
        title = font.render("PONG", True, WHITE)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 4))
        self._draw_gradient_text(self.screen, "PONG", font, title_rect, WHITE, BLUE)

        # Draw options with hover effect and gradient
        for i, option in enumerate(self.options):
            color = BLUE if i == self.selected_option else WHITE
            font = pygame.font.Font(None, option_size)
            text = font.render(option, True, color)
            rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + i * 60))
            self._draw_gradient_text(self.screen, option, font, rect, WHITE, BLUE)

            # Draw selection indicator
            if i == self.selected_option:
                pygame.draw.rect(self.screen, BLUE, (rect.left - 20, rect.centery - 2, 10, 4))
                pygame.draw.rect(self.screen, BLUE, (rect.right + 10, rect.centery - 2, 10, 4))

        # Draw instruction text at bottom
        instruction_font = pygame.font.Font(None, 30)
        instructions = [
            "ARROWS UP/DOWN - Move Selection",
            "ENTER - Select Option"
        ]
        for i, instruction in enumerate(instructions):
            text = instruction_font.render(instruction, True, GRAY)
            rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50 + i * 25))
            self.screen.blit(text, rect)

    def _draw_controls(self):
        controls = [
            "HOW TO PLAY",
            "",
            "Player 1 (Blue):",
            "W - Move Up",
            "S - Move Down",
            "",
            "Player 2 (Red):",
            "UP - Move Up",
            "DOWN - Move Down",
            "",
            "ESC - Pause Game",
            "",
            "Press ENTER to return"
        ]

        for i, line in enumerate(controls):
            color = BLUE if i == 0 else WHITE
            size = 50 if i == 0 else 36
            font = pygame.font.Font(None, size)
            text = font.render(line, True, color)
            rect = text.get_rect(center=(WINDOW_WIDTH // 2, 100 + i * 40))
            self.screen.blit(text, rect)

    def _draw_gradient_text(self, screen, text, font, rect, color1, color2):
        """Draw text with a gradient effect."""
        text_surface = font.render(text, True, color1)
        gradient_surface = pygame.Surface(text_surface.get_size(), pygame.SRCALPHA)
        width, height = text_surface.get_size()

        for y in range(height):
            blend_ratio = y / height
            blended_color = (
                int(color1[0] * (1 - blend_ratio) + color2[0] * blend_ratio),
                int(color1[1] * (1 - blend_ratio) + color2[1] * blend_ratio),
                int(color1[2] * (1 - blend_ratio) + color2[2] * blend_ratio),
                255
            )
            pygame.draw.line(gradient_surface, blended_color, (0, y), (width, y))

        text_surface.blit(gradient_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(text_surface, rect)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            if event.type == pygame.KEYDOWN:
                if self.showing_controls:
                    if event.key == pygame.K_RETURN:
                        self.showing_controls = False
                else:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        if self.options[self.selected_option] == "HOW TO PLAY":
                            self.showing_controls = True
                            return None
                        return self.options[self.selected_option]
        return None
