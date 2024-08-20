1. Game Setup:
- Screen Setup:
  - Screen dimensions are set to 960x720.
  - Colors are defined in RGB format (e.g., black and white).
- Initialization:
  - pygame.init() initializes the Pygame library, which is necessary for running the game.
  - screen = pygame.display.set_mode(...) creates the game window.
  - pygame.display.set_caption('Pong') sets the window title to "Pong".

2. Game Elements:
- Paddles and Ball:
  - Paddles (paddle_1_rect, paddle_2_rect) are created as rectangular objects with a specific position and size.
  - The ball (ball_rect) is also a rectangle, positioned in the center of the screen initially.
- Movement:
  - Variables paddle_1_move and paddle_2_move are used to track the movement of each paddle.

3. Ball Reset Function (reset_ball()):
- Position Reset:
  - The ball's position is reset to the center of the screen.
- Random Speed and Direction:
  - The ball's speed (ball_accel_x, ball_accel_y) is set randomly within a certain range.
  - The direction of the ball is randomized.
- Returning State:
  - The function returns the new speed values and a flag (started) indicating whether the game has started.

4. Game Loop:
- Event Handling:
  - The game loop handles user inputs (e.g., pressing keys) to move paddles or start the game.
- Movement and Collision:
  - Paddles move based on user input.
  - The ball bounces off the top and bottom edges of the screen and the paddles.
- Score Handling:
  - The scores are updated when the ball goes out of bounds on either side.
- Ball Reset After Scoring:
  - The ball is reset to the center after a score, with new random speed and direction.

5. Rendering:
- Drawing Elements:
  - The paddles, ball, and scores are drawn to the screen using pygame.draw.rect() and screen.blit() for the text.
- Screen Update:
  - pygame.display.update() updates the display with the latest drawn elements, effectively refreshing the screen.
  
6. Frame Rate Control:
- Clock:
  - clock.tick(60) is used to control the game's frame rate, ensuring smooth movement and consistent timing at 60 FPS.