import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_SPEED = 5
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 60
PADDLE_SPEED = 7

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Ball and paddle positions
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x, ball_speed_y = BALL_SPEED, BALL_SPEED

left_paddle_x, right_paddle_x = 10, WIDTH - 25
left_paddle_y, right_paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2, HEIGHT // 2 - PADDLE_HEIGHT // 2

# Scores
score_left, score_right = 0, 0

# Font for displaying the score
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

def reset_ball():
    """Reset the ball to the center."""
    return WIDTH // 2, HEIGHT // 2, BALL_SPEED, BALL_SPEED

# Game Loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle_y < HEIGHT - PADDLE_HEIGHT:
        left_paddle_y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle_y < HEIGHT - PADDLE_HEIGHT:
        right_paddle_y += PADDLE_SPEED

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with paddles
    if (left_paddle_x < ball_x < left_paddle_x + PADDLE_WIDTH and left_paddle_y < ball_y < left_paddle_y + PADDLE_HEIGHT) or \
       (right_paddle_x < ball_x < right_paddle_x + PADDLE_WIDTH and right_paddle_y < ball_y < right_paddle_y + PADDLE_HEIGHT):
        ball_speed_x = -ball_speed_x

    # Ball collision with walls
    if ball_y <= 0 or ball_y >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # Scoring
    if ball_x <= 0:
        score_right += 1
        ball_x, ball_y, ball_speed_x, ball_speed_y = reset_ball()

    if ball_x >= WIDTH:
        score_left += 1
        ball_x, ball_y, ball_speed_x, ball_speed_y = reset_ball()

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (left_paddle_x, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (right_paddle_x, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x - 10, ball_y - 10, 20, 20))

    # Display scores
    score_display = font.render(f"{score_left} - {score_right}", True, WHITE)
    screen.blit(score_display, (WIDTH // 2 - 40, 10))

    pygame.display.flip()
    clock.tick(60)
