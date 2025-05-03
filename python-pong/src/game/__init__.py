"""
Game Package
------------
This package contains the core components of the Pong game, including:
- Paddle: Player and AI-controlled paddles.
- Ball: The ball logic and movement.
- Menu: The game menu and UI.
"""

__author__ = "Mr.Dev"
__version__ = "0.3"

# Expose key classes for easier imports
from .paddle import Paddle
from .ai_paddle import AIPaddle
from .ball import Ball
from .menu import Menu
