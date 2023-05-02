import pygame
import random

# initialize pygame
pygame.init()

# set up the display
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# snake variables
snake_size = 10
snake_speed = 15

# font
font_style = pygame.font.SysFont(None, 30) # type: ignore

# create snake


def create_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_size, snake_size])

# display score


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

# game loop
def gameLoop():
    game_over = False
    game_close = False

    # initial position of snake
    x1 = width / 2
    y1 = height / 2

    # change in position of snake
    x1_change = 0
    y1_change = 0

    # snake list
    snake_List = []
    Length_of_snake = 1

    # initial food position
    foodx = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    # define clock variable
    clock = pygame.time.Clock()

    while not game_over:

        while game_close == True:
            screen.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0

        # check if snake hits the boundary
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # update position of snake
        x1 += x1_change
        y1 += y1_change

        # fill screen with white color
        screen.fill(white)

        # draw food
        pygame.draw.rect(screen, red, [foodx,foody, snake_size, snake_size]) # type: ignore

        # update snake
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # check if snake hits itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # create snake
        create_snake(snake_size, snake_List)

        # update score
        pygame.display.update()

        # check if snake eats food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(
                0, width - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(
                0, height - snake_size) / 10.0) * 10.0
            Length_of_snake += 1

        # update game speed using clock.tick()
        clock.tick(snake_speed)

    # quit pygame
    pygame.quit()

    # quit python
    quit()


# start game
gameLoop()
