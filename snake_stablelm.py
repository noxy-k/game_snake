import pygame

# Define the snake and coordinates
snake = pygame.snakes.Rectangle((0, 0), pygame.Rect(400, 200))
coords = (200, 200)

# Define the game logic


def moving(event):
    screen.fill((0, 0, 0))
    screen.blit(snake, (200, 200))
    screen.blit(coords, (300, 300))
    screen.blit(pygame.key.get_pressed())
    pygame.key.quit()


# Main game loop
running = True
while running:
    # Capture the input
    game_input = pygame.input.get()

    # Move the snake
    snake.position.x = game_input.getkey() - 30
    snake.position.y = game_input.getkey() - 25
    snake.position.z = game_input.getkey() + 50

    # Calculate the new position of the snake
    new_snake_position = snake.position + coords

    # Update the snake's position
    snake.velocity.x = -5
    snake.velocity.z = 5
