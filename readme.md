## Requirements

- Python 3.x
- Pygame

You can install the required packages using pip:

```bash
pip install pygame
```

## How It Works

This is a simple Pong game implemented in Python using the Pygame library. The game features two paddles controlled by different players and a ball that bounces off the paddles and the screen's top and bottom edges. The objective is to score points by getting the ball past the opponent's paddle.

### Game Controls

- Player 1 (Left Paddle):
  - Move Up: Press W
  - Move Down: Press S
- Player 2 (Right Paddle):
  - Move Up: Press the Up Arrow
  - Move Down: Press the Down Arrow
 - Start the Game: Press Spacebar

### Running the Game
To run the game, execute the script:

  ```bash
python main.py
```

The Pygame window will open, displaying the grid and the current state of the cells.

## Code Overview

### 1. Game Setup:
- Screen Setup:
  - Screen dimensions are set to 960x720.
  - Colors are defined in RGB format (e.g., black and white).
- Initialization:
  - pygame.init() initializes the Pygame library, which is necessary for running the game.
  - screen = pygame.display.set_mode(...) creates the game window.
  - pygame.display.set_caption('Pong') sets the window title to "Pong".

### 2. Game Elements:
- Paddles and Ball:
  - Paddles (paddle_1_rect, paddle_2_rect) are created as rectangular objects with a specific position and size.
  - The ball (ball_rect) is also a rectangle, positioned in the center of the screen initially.
- Movement:
  - Variables paddle_1_move and paddle_2_move are used to track the movement of each paddle.

### 3. Ball Reset Function (reset_ball()):
- Position Reset:
  - The ball's position is reset to the center of the screen.
- Random Speed and Direction:
  - The ball's speed (ball_accel_x, ball_accel_y) is set randomly within a certain range.
  - The direction of the ball is randomized.
- Returning State:
  - The function returns the new speed values and a flag (started) indicating whether the game has started.

### 4. Game Loop:
- Event Handling:
  - The game loop handles user inputs (e.g., pressing keys) to move paddles or start the game.
- Movement and Collision:
  - Paddles move based on user input.
  - The ball bounces off the top and bottom edges of the screen and the paddles.
- Score Handling:
  - The scores are updated when the ball goes out of bounds on either side.
- Ball Reset After Scoring:
  - The ball is reset to the center after a score, with new random speed and direction.

### 5. Rendering:
- Drawing Elements:
  - The paddles, ball, and scores are drawn to the screen using pygame.draw.rect() and screen.blit() for the text.
- Screen Update:
  - pygame.display.update() updates the display with the latest drawn elements, effectively refreshing the screen.
  
### 6. Frame Rate Control:
- Clock:
  - clock.tick(60) is used to control the game's frame rate, ensuring smooth movement and consistent timing at 60 FPS.
