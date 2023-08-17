import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake and food
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (WIDTH//10)) * 10,
            random.randrange(1, (HEIGHT//10)) * 10]
food_spawn = True

# Directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
direction = RIGHT
change_to = direction

# Game over flag
game_over = False

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Change direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = UP
            if event.key == pygame.K_DOWN:
                change_to = DOWN
            if event.key == pygame.K_LEFT:
                change_to = LEFT
            if event.key == pygame.K_RIGHT:
                change_to = RIGHT

    # Validation of direction
    if change_to == UP and direction != DOWN:
        direction = UP
    if change_to == DOWN and direction != UP:
        direction = DOWN
    if change_to == LEFT and direction != RIGHT:
        direction = LEFT
    if change_to == RIGHT and direction != LEFT:
        direction = RIGHT

    # Moving the snake
    if direction == UP:
        snake_pos[1] -= 10
    if direction == DOWN:
        snake_pos[1] += 10
    if direction == LEFT:
        snake_pos[0] -= 10
    if direction == RIGHT:
        snake_pos[0] += 10

    # Snake body growing mechanism
        snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//10)) * 10,
                    random.randrange(1, (HEIGHT//10)) * 10]
    food_spawn = True

    # Draw snake and food
    screen.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, RED, pygame.Rect(
        food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH-10:
        game_over = True
    if snake_pos[1] < 0 or snake_pos[1] > HEIGHT-10:
        game_over = True

    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over = True

    pygame.display.update()
    clock.tick(15)  # 15 FPS

# Quit the game
pygame.quit()
quit()
