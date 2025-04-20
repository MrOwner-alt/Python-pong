# python-pong/README.md

# Python Pong Game

This is a simple Pong game implemented in Python using the Pygame library. The game features two paddles and a ball, where players can control the paddles to hit the ball back and forth.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/python-pong.git
   cd python-pong
   ```

2. **Install the required dependencies:**
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game:**
   Execute the following command to start the game:
   ```bash
   python src/main.py
   ```

## Gameplay

- Use the arrow keys to control the right paddle.
- Use the 'W' and 'S' keys to control the left paddle.
- The objective is to score points by getting the ball past the opponent's paddle.

## File Structure

```
python-pong
├── src
│   ├── main.py
│   ├── game
│   │   ├── __init__.py
│   │   ├── ball.py
│   │   ├── paddle.py
│   │   └── game.py
│   └── utils
│       ├── __init__.py
│       └── constants.py
├── tests
│   ├── __init__.py
│   ├── test_ball.py
│   └── test_paddle.py
├── requirements.txt
└── README.md
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
