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
        self.image = right_img # make the player the player image
        self.image.set_colorkey(BLACK) #ignore blcak pixels of player image
        self.rect = self.image.get_rect() 
        self.rect.center = (WIDTH / 2, HEIGHT / 2) # set the sprite initial position
    
    #checks the state of the key board and adjusts the sprite according
    def update(self, direction):
        if pressed[pygame.K_UP]: #up key pressed
            self.rect.y -= 5
        if pressed[pygame.K_DOWN]: #down key pressed
            self.rect.y += 5
        if pressed[pygame.K_LEFT]: #left key pressed
            self.image = left_img
            self.image.set_colorkey(BLACK) #ignore blcak pixels 
            self.rect.x -= 5
        if pressed[pygame.K_RIGHT]: #right key pressed
            self.image = right_img
            self.image.set_colorkey(BLACK) #ignore blcak pixels 
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
class bottle(pygame.sprite.Sprite):
    def __init__(self): #initialize all of the attributes for the trash sprite
        pygame.sprite.Sprite.__init__(self) #super init
        self.image = bottle_img # make the trash the trash image
        self.image.set_colorkey(BLACK) #ignore blcak pixels of trash image
        self.rect = self.image.get_rect() 
        self.rect.center = (random.randint(1, WIDTH - 9),random.randint(1, HEIGHT - 49)) #randomly place the bottle on the screen
#make the can sprite
class can(pygame.sprite.Sprite):
    def __init__(self): #initialize all of the attributes for the trash sprite
        pygame.sprite.Sprite.__init__(self) #super init
        self.image = can_img # make the can the can image
        self.image.set_colorkey(BLACK) #ignore blcak pixels of can image
        self.rect = self.image.get_rect() 
        self.rect.center = (random.randint(1, WIDTH - 9),random.randint(1, HEIGHT - 49)) #randomly place the can on the screen

# initialize pygame and create window
pygame.init()
pygame.mixer.init()  # for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #create the display
pygame.display.set_caption("Trash Game") #set caption
clock = pygame.time.Clock() 
right_img = pygame.image.load(os.path.join(img_folder, 'right.png')).convert()
left_img = pygame.image.load(os.path.join(img_folder, 'left.png')).convert()
bottle_img = pygame.image.load(os.path.join(img_folder, 'bottle.png')).convert()
can_img = pygame.image.load(os.path.join(img_folder, 'can.png')).convert()

numTrash = 6 #remove later and set for each level
 
playerSprites = pygame.sprite.Group() #group of player sprites could be 2 player eventually
trashSprites = pygame.sprite.Group() #group of all bottlr sprites
player = Player() #make a new player sprite
playerSprites.add(player) #add the player to the player sprites group

for i in range(numTrash):
    if (i < 3):
        trash = bottle()
        trashSprites.add(trash)
    else:
        trash = can()
        trashSprites.add(trash)

score = 0
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
    if (pygame.sprite.spritecollide(player, trashSprites, True)):
        score += 1
    # Render (draw)
    screen.fill(BLACK)
    playerSprites.draw(screen)
    trashSprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
print score