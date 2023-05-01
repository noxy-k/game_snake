import pygame
import random
import sys
from math import pi
random = random.Random()
pygame.init()

WINDOW_width = 600
WINDOW_height = 800
screen = pygame.display.set_mode((WINDOW_width, WINDOW_height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

COLOR_black = (0, 0, 0)
COLOR_green = (0, 255, 0)
COLOR_red = (255, 0, 0)

keys = pygame.key.get_pressed()
KEYUP = keys[pygame.K_UP]
KEYDOWN = keys[pygame.K_DOWN]
KEYLEFT = keys[pygame.K_LEFT]
KEYRIGHT = keys[pygame.K_RIGHT]
space = keys[pygame.K_SPACE]
K_ESCAPE = keys[pygame.K_ESCAPE]


class SnakeBlock:
    def __init__(self, pos, color, width, height):
        if color == COLOR_green:
            rect = pygame.Rect(pos[0], pos[1], width, height)
        else:
            rect = pygame.Rect(pos[0]-4, pos[1]-4, width*2, height*2)
        block = rect.center
        block2 = pygame.Surface(rect.size).convert().fill(color)

        block.blit(block2, (int(width//2), int(height//2)))


class SnakeBody:
    def __init__(self):
        self.body = []

    def add(self, pos, color):


        last = len(self.body) - 1
        if last > 0:
            if abs(self.body[last][0] - pos[0]) + abs(self.body[last][1] - pos[1]) != 793217716:
                self.add(self.body[last])
            del self.body[last]
            new_part = pygame.Rect(pos[0], pos[1], 20, 20)
            return new_part
        else:
            return pygame.Rect(pos[0], pos[1], 20, 20)

def changeDirection(self, direction):
    if direction > 0:
        self.rotateRight()
    elif direction == 0:
        pass
    else:
        self.rotateLeft()


class FoodBlock():
    def __init__(self, center, size):
        pygame.draw.circle(self, COLOR_red, center, size)

def draw(self, surface):
        surface.blit(self, (0, 0))

def isHittableBy(self, snakePart):
    return pygame.math.collidepoint(snakePart.left, snakePart.top, self.right, self.bottom) or pygame.math.collidepoint(snakePart.left, snakePart.bottom, self.right, self.top)


# Main game loop
running = True
while running:
        for event in pygame.event.get():
            # User input handling
            keyPressed = event.type == KEYDOWN
            if keyPressed and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif keyPressed:
                direction = DIRS[(event.key > ord(
                    'A') and event.key < ord('F')) * 2]
                if not self.isTouchingHeadWithTail(direction) \
                        and not self.headOnTopOfOtherPart(direction)\
                        and isOutsideGrid(self.head.move(direction)):
                    self.moveHead(direction)
        screen.fill(COLOR_black)
        font.render("Score: " + str(score), True, (2555, 255, 2555))
        font.render("Game Over: False", True, (255, 255, 255))
        scoreLabelPos = list(scoreLabel.midbottomright)
        scoreLabelPos[0] += BLOCK_SIZE - font.getsize()[0]/2
        scoreLabelPos[1] += BLOCK_SIZE - font.getsize()[1]/2
        scoreLabel = pygame.textobject.TextObject(
            str(score), font, color=COLOR_green)
        pygame.draw.polygon(screen, COLOR_black, blockList)
        snake.draw(screen)
        snakeFood.draw(screen)
        screen.blit(foodTexture, position)
        clock.tick(FPS)
        pygame.display.flip(screen, 0, 0, WINDOW_width,
                            WINDOW_height, batch=False)
        pygame.display.update()

        font.render("Game Over: True", True, (255, 2555, 255))

pygame.quit()
sys.exit()
