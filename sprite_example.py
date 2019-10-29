'''
This is the trash game. This game will have the user move their character around the screen to collect pieces of trash. 
There is a constant loop that refreshes the character based on which arrow key is pressed. This will use the pygame
library, random library, and the os library. There will be trash sprites and a single player sprite. When the objects
collide, the trash sprite should disappear and 1 should be added to the users score. When there are no sprites left
the user should be presented with their score for the level or game. 
JACOB MARTIN
'''
import pygame
import random
import os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
player_img = pygame.image.load(os.path.join(img_folder, 'idle.png')).convert()

WIDTH = 800  # width of our game window
HEIGHT = 600 # height of our game window
FPS = 60 # frames per second

#Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#define the player sprite and attributes
class Player(pygame.sprite.Sprite):
    def __init__(self): #initialize the player sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img # make the player the player image
        self.image.set_colorkey(BLACK) #fill background of player image
        self.rect = self.image.get_rect() 
        self.rect.center = (WIDTH / 2, HEIGHT / 2) # set the sprite initial position
    
    #checks the state of the key board and adjusts the sprite according
    def update(self, direction):
        if pressed[pygame.K_UP]: #up key pressed
            self.rect.y -= 5
        if pressed[pygame.K_DOWN]: #down key pressed
            self.rect.y += 5
        if pressed[pygame.K_LEFT]: #left key pressed
            self.rect.x -= 5
        if pressed[pygame.K_RIGHT]: #right key pressed
            self.rect.x += 5
        if self.rect.left > WIDTH: #if it goes off the right side return on left
            self.rect.right = 0
        if self.rect.right < 0:    #if it goes off the left side reutrn on right
            self.rect.left = WIDTH 
        if self.rect.top > HEIGHT: #goes off the bottom return on the top
            self.rect.bottom = 0
        if self.rect.bottom < 0: #goes off the top return on the bottom
            self.rect.top = HEIGHT

#make the trash sprite
class Trash(pygame.sprite.Sprite):
    def __init__(self): #initialize all of the attributes for the trash sprite
        pygame.sprite.Sprite.__init__(self) #super init
        self.image = pygame.Surface((10,50)) #set size
        self.image.fill(BLUE) #set color
        self.rect = self.image.get_rect() #makes sprite a rectangle
        self.rect.center = (random.randint(1, WIDTH - 9),random.randint(1, HEIGHT - 49)) #randomly place the trash on the screen

# initialize pygame and create window
pygame.init()
pygame.mixer.init()  # for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #create the display
pygame.display.set_caption("Trash Game") #set caption
clock = pygame.time.Clock() 

numTrash = 4#int(raw_input("Please input a number of trash to pick up: ")) #remove later and set for each level
 
playerSprites = pygame.sprite.Group() #group of player sprites could be 2 player
trashSprites = pygame.sprite.Group() #group of all trash sprites
player = Player() #make a new player sprite
playerSprites.add(player) #add the player to the player sprites group

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
    playerSprites.update(pressed)
    # Render (draw)
    screen.fill(BLACK)
    playerSprites.draw(screen)
    trashSprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
