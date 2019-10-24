# Pygame template - skeleton for a new pygame project
import pygame
import random
import os

WIDTH = 800  # width of our game window
HEIGHT = 600 # height of our game window
FPS = 60 # frames per second

#Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
    
    def update(self, direction):
        if pressed[pygame.K_UP]: 
            self.rect.y -= 5
        if pressed[pygame.K_DOWN]: 
            self.rect.y += 5
        if pressed[pygame.K_LEFT]: 
            self.rect.x -= 5
        if pressed[pygame.K_RIGHT]:
            self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = WIDTH 
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = HEIGHT

class Trash(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(1, WIDTH - 9),random.randint(1, HEIGHT - 49))

# initialize pygame and create window
pygame.init()
pygame.mixer.init()  # for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

numTrash = int(raw_input("Please input a number of trash to pick up: "))
 
gameSprite = pygame.sprite.Group()
trashSprites = pygame.sprite.Group()
player = Player()
gameSprite.add(player)

for i in range(numTrash):
    trash = Trash()
    trashSprites.add(trash)
# Game Loop
running = True
while running:
    
    #keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False
    # Update
    pressed = pygame.key.get_pressed()
    gameSprite.update(pressed)
    #trashSprites.update()
    # Render (draw)
    screen.fill(BLACK)
    gameSprite.draw(screen)
    trashSprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()