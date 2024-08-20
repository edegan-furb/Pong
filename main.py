import pygame
import random

# constants for the windows width and height values
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

# the RGB values for the colors used in the game
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

def main(): 
    # GAME SETUP
    
    # initialize the PyGame library (this is absolutely necessary)
    pygame.init()

    # this creates the window for the game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # set the window's title
    pygame.display.set_caption('Pong')

    # create the clock object to keep track of the time
    clock = pygame.time.Clock()
    
    # Load the Consolas font
    font = pygame.font.SysFont('Consolas', 30)
    
    # Scores
    score_player_1 = 0
    score_player_2 = 0

    def reset_ball():
        # Reset the ball's position
        ball_rect.x = SCREEN_WIDTH / 2
        ball_rect.y = SCREEN_HEIGHT / 2
        
        # Reset the ball's speed
        ball_accel_x = random.randint(2, 4) * 0.1
        ball_accel_y = random.randint(2, 4) * 0.1
        
        # Randomize the direction of the ball
        if random.randint(1, 2) == 1:
            ball_accel_x *= -1
        if random.randint(1, 2) == 1:
            ball_accel_y *= -1
        
        # Pause before the ball starts moving again
        return ball_accel_x, ball_accel_y, False
    
    '''
    these are the players' game paddles
    the `Rect` function needs the x, y, width and height
    of the rectangles we will be drawing
    '''
    paddle_1_rect = pygame.Rect(30, 0, 7, 100)
    paddle_2_rect = pygame.Rect(SCREEN_WIDTH - 50, 0, 7, 100)

    # This is to track by how much the players' paddles will move per frame
    paddle_1_move = 0
    paddle_2_move = 0

    # Initialize the ball
    ball_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 25, 25)
    ball_accel_x, ball_accel_y, started = reset_ball()

    # GAME LOOP
    while True:
        
        ''' 
        Set the background color to black
        Needs to be called every time the game updates
        '''
        screen.fill(COLOR_BLACK)
        
        # Display the scores
        score_text = font.render(f"{score_player_1} - {score_player_2}", True, COLOR_WHITE)
        score_text_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 50))
        screen.blit(score_text, score_text_rect)
        
        # Make the ball move after 3 seconds
        if not started:
            text = font.render('Press Space to Start', True, COLOR_WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text, text_rect)
            pygame.display.flip()
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        started = True
            continue

        '''
        Get the time elapse between now and the last frame
        60 is an arbitrary number but the game runs smooth at 60 FPS
        '''
        delta_time = clock.tick(60)

        # Checking for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                # PLAYER 1
                if event.key == pygame.K_w:
                    paddle_1_move = -0.5
                if event.key == pygame.K_s:
                    paddle_1_move = 0.5

                # PLAYER 2
                if event.key == pygame.K_UP:
                    paddle_2_move = -0.5
                if event.key == pygame.K_DOWN:
                    paddle_2_move = 0.5

            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_w, pygame.K_s):
                    paddle_1_move = 0.0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    paddle_2_move = 0.0

        # Move paddle_1 and paddle_2 according to their `move` variables
        paddle_1_rect.top += paddle_1_move * delta_time
        paddle_2_rect.top += paddle_2_move * delta_time

        # Prevent paddles from going out of bounds
        paddle_1_rect.top = max(0, min(paddle_1_rect.top, SCREEN_HEIGHT - paddle_1_rect.height))
        paddle_2_rect.top = max(0, min(paddle_2_rect.top, SCREEN_HEIGHT - paddle_2_rect.height))

        # Ball collision with top and bottom
        if ball_rect.top < 0 or ball_rect.bottom > SCREEN_HEIGHT:
            ball_accel_y *= -1

        # Ball collision with paddles
        if paddle_1_rect.colliderect(ball_rect) and ball_accel_x < 0:
            ball_accel_x *= -1
            ball_rect.left = paddle_1_rect.right + 5
        if paddle_2_rect.colliderect(ball_rect) and ball_accel_x > 0:
            ball_accel_x *= -1
            ball_rect.right = paddle_2_rect.left - 5

        # Update ball position
        if started:
            ball_rect.left += ball_accel_x * delta_time
            ball_rect.top += ball_accel_y * delta_time

        # Check if the ball goes out of bounds and update scores
        if ball_rect.left <= 0:
            score_player_2 += 1
            ball_accel_x, ball_accel_y, started = reset_ball()
        elif ball_rect.right >= SCREEN_WIDTH:
            score_player_1 += 1
            ball_accel_x, ball_accel_y, started = reset_ball()

        # Draw paddles and ball
        pygame.draw.rect(screen, COLOR_WHITE, paddle_1_rect)
        pygame.draw.rect(screen, COLOR_WHITE, paddle_2_rect)
        pygame.draw.rect(screen, COLOR_WHITE, ball_rect)

        # Update the display
        pygame.display.update()

# Run the game
if __name__ == '__main__':
    main()
