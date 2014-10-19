import pygame, sys
from pygame.locals import *
from random import randint


img1 = "img1.png"
img2 = "img2.png"
bket = "bucket.png"
bkgd = "bkgrnd.jpg"

pygame.init()
screen = pygame.display.set_mode((650,350), 0, 32)
background = pygame.image.load(bkgd).convert()

image1 = pygame.image.load(img1).convert_alpha()
image2 = pygame.image.load(img2).convert_alpha()
bucket = pygame.image.load(bket).convert_alpha()

pos1, pos2 = randint(0, 575), randint(0, 575)
score = 0
y = 0
y1 = 0
bucket_x, bucket_y = 0, 275
mouse_x, mouse_y = 0, 0

clock = pygame.time.Clock()
speed = 200

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(background, (0, 0))
    screen.blit(image1, (pos1, y))
    screen.blit(image2, (pos2, y1))
    milli = clock.tick()
    seconds = milli/1000.
    dm = speed * seconds
    y += dm
    y1 += dm
    
    if y > 350:
        y = 0
        pos1 = randint(0, 575)
    if y1 > 350:
        y1 = 0
        pos2 = randint(0, 575)
        
    mouse_x, mouse_y = pygame.mouse.get_pos()
    disp_x = mouse_x - bucket.get_width()/2
    screen.blit(bucket, (disp_x, bucket_y))
    
    if mouse_x > pos1 and mouse_x < (pos1 + 60):
        if y > 260:
            score += 1
            pos1 = randint(0, 575)
            y = 0
            
    if mouse_x > pos2 and mouse_x < (pos2 + 60):
        if y1 > 260 :
            score += 1
            pos2 = randint(0, 575)
            y1 = 0
            
    pygame.display.update()
    
    