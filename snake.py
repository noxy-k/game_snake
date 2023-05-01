import pygame
import sys
import random
from pygame.locals import *

# Constants
FPS = 10
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELL_SIZE = 20
assert WINDOW_WIDTH % CELL_SIZE == 0, "Window width must be a multiple of cell size."
assert WINDOW_HEIGHT % CELL_SIZE == 0, "Window height must be a multiple of cell size."
CELL_WIDTH = WINDOW_WIDTH // CELL_SIZE
CELL_HEIGHT = WINDOW_HEIGHT // CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Directions
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0  # Index of the snake's head


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Snake')

    while True:
        run_game()
        show_game_over_screen()


def run_game():
    start_x = random.randint(5, CELL_WIDTH - 6)
    start_y = random.randint(5, CELL_HEIGHT - 6)
    snake_coords = [{'x': start_x, 'y': start_y},
                    {'x': start_x - 1, 'y': start_y},
                    {'x': start_x - 2, 'y': start_y}]
    direction = RIGHT

    # Place the apple in a random location
    apple = get_random_location()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif event.key == K_ESCAPE:
                    terminate()

        # Check if the snake has hit the edge or itself
        if snake_coords[HEAD]['x'] == -1 or snake_coords[HEAD]['x'] == CELL_WIDTH or snake_coords[HEAD]['y'] == -1 or snake_coords[HEAD]['y'] == CELL_HEIGHT:
            return
        for snake_body in snake_coords[1:]:
            if snake_body['x'] == snake_coords[HEAD]['x'] and snake_body['y'] == snake_coords[HEAD]['y']:
                return

        # Check if the snake has eaten the apple
        if snake_coords[HEAD]['x'] == apple['x'] and snake_coords[HEAD]['y'] == apple['y']:
            apple = get_random_location()
        else:
            del snake_coords[-1]

        # Move the snake
        if direction == UP:
            new_head = {'x': snake_coords[HEAD]['x'],
                        'y': snake_coords[HEAD]['y'] - 1}
        elif direction == DOWN:
            new_head = {'x': snake_coords[HEAD]['x'],
                        'y': snake_coords[HEAD]['y'] + 1}
        elif direction == LEFT:
            new_head = {'x': snake_coords[HEAD]
                        ['x'] - 1, 'y': snake_coords[HEAD]['y']}
        elif direction == RIGHT:
            new_head = {'x': snake_coords[HEAD]
                        ['x'] + 1, 'y': snake_coords[HEAD]['y']}
        snake_coords.insert(0, new_head)

        DISPLAYSURF.fill(BLACK)
        # uncomment this line to draw the grid
        # draw_grid()
        draw_snake(snake_coords)
        draw_apple(apple)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def draw_grid():
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(DISPLAYSURF, WHITE, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(DISPLAYSURF, WHITE, (0, y), (WINDOW_WIDTH, y))


def draw_snake(snake_coords):
    for coord in snake_coords:
        x = coord['x'] * CELL_SIZE
        y = coord['y'] * CELL_SIZE
        snake_segment_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(DISPLAYSURF, GREEN, snake_segment_rect)
        # uncomment this line to see the border around the snake segments
        # pygame.draw.rect(DISPLAYSURF, WHITE, snake_segment_rect, 1)


def draw_apple(coord):
    x = coord['x'] * CELL_SIZE
    y = coord['y'] * CELL_SIZE
    apple_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(DISPLAYSURF, RED, apple_rect)
    # uncomment this line to see the border around the apple
    # pygame.draw.rect(DISPLAYSURF, WHITE, apple_rect, 1)


def get_random_location():
    return {'x': random.randint(0, CELL_WIDTH - 1), 'y': random.randint(0, CELL_HEIGHT - 1)}


def show_game_over_screen():
    game_over_font = pygame.font.Font(None, 48)
    game_over_surf = game_over_font.render('Game Over', True, WHITE)
    game_over_rect = game_over_surf.get_rect()
    game_over_rect.midtop = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50)

    DISPLAYSURF.blit(game_over_surf, game_over_rect)
    pygame.display.update()
    pygame.time.wait(2000)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                terminate()
            elif event.type == KEYDOWN and (event.key == K_RETURN or event.key == K_SPACE):
                return


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
