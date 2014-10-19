import pygame, sys
from pygame.locals import *
from random import randint
import time

screen_height, screen_width = 350, 650


img1 = "img1.png"
img2 = "img2.png"
img3 = "img3.png"
img4 = "img4.png"
bket = "bucket.png"
bkgd = "bkgrnd.jpg"


def display():
    score = 0
    clock = pygame.time.Clock()
    speed1 = 100 
    speed2 = 150
    speed3 = 170
    speed4 = 200
    speed_inc = True
    pygame.init()
    screen = pygame.display.set_mode((650,350), 0, 32)
    
    background = pygame.image.load(bkgd).convert()
    image1 = pygame.image.load(img1).convert_alpha()
    image2 = pygame.image.load(img2).convert_alpha()
    image3 = pygame.image.load(img3).convert_alpha()
    image4 = pygame.image.load(img4).convert_alpha()    
    bucket = pygame.image.load(bket).convert_alpha()    
    
    image1_x, image2_x, image3_x, image4_x = get_position(), get_position(), get_position(), get_position()
    image1_y, image2_y, image3_y, image4_y = 0, 0, 0, 0
    bucket_x, bucket_y = 0, 275
    mouse_x, mouse_y = 0, 0   
    
    start = time.time()


    while time.time() - start < 45:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()   
                
        screen.blit(background, (0, 0))
        screen.blit(image1, (image1_x, image1_y))
        screen.blit(image2, (image2_x, image2_y))
        screen.blit(image3, (image3_x, image3_y))
        screen.blit(image4, (image4_x, image4_y))        
        screen.blit(bucket, (bucket_x, bucket_y))
        
        milli = clock.tick()
        seconds = milli/1000.
        dm1 = speed1 * seconds
        dm2 = speed2 * seconds
        dm3 = speed3 * seconds
        dm4 = speed4 * seconds
        
        image1_x, image1_y = image1_display(dm1, image1_x, image1_y, screen)
        image2_x, image2_y = image2_display(dm2, image2_x, image2_y, screen)
        image3_x, image3_y = image3_display(dm3, image3_x, image3_y, screen)
        image4_x, image4_y = image4_display(dm4, image4_x, image4_y, screen)        
    
    
        mouse_x, mouse_y = pygame.mouse.get_pos()
        bucket_x = mouse_x - bucket.get_width()/2
        
        if mouse_x > image1_x and mouse_x < (image1_x + 60):
            if image1_y > 270 and image1_y < 310:
                score += 1
                image1_x = get_position()
                image1_y = -200
                
        if mouse_x > image2_x and mouse_x < (image2_x + 60):
            if image2_y > 270 and image2_y < 310:
                score += 1
                image2_x = get_position()
                image2_y = -200  
                
                
        if mouse_x > image3_x and mouse_x < (image3_x + 60):
            if image3_y > 270 and image3_y < 310:
                score += 1
                image3_x = get_position()
                image3_y = -250
                
        if mouse_x > image4_x and mouse_x < (image4_x + 60):
            if image4_y > 270 and image4_y < 310:
                score += 1
                image4_x = get_position()
                image4_y = -300                 

        if time.time() - start > 30 and speed_inc:
            speed1 += 100 
            speed2 += 100
            speed3 += 100
            speed4 += 100   
            speed_inc = False    
            
            
        myfont = pygame.font.SysFont(None, 18)
        label1 = myfont.render(("Time:"+str(int(time.time() - start ))), 1, (0, 255, 255))
        label2 = myfont.render(("Score:"+str(score)), 1, (0, 255, 255))
        screen.blit(label1, (0, 0))
        screen.blit(label2, (0, 18))
        pygame.display.update()
        
    myfont = pygame.font.SysFont(None, 32)
    label = myfont.render(("Score:"+str(score)), 1, (0, 255, 255))
    while True:
        screen.blit(background, (0, 0))
        screen.blit(label, (300, 150))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()     
  
        

def image1_display(dm, image1_x, image1_y, screen):
    
    if image1_y > 350:
        image1_y = -200
        image1_x = get_position()  
    else:
        image1_y += dm
        
    return image1_x, image1_y


def image2_display(dm, image2_x, image2_y, screen):
    
    if image2_y > 350:
        image2_y = -300
        image2_x = get_position()  
    else:
        image2_y += dm
        
    return image2_x, image2_y

def image3_display(dm, image3_x, image3_y, screen):
    
    if image3_y > 350:
        image3_y = -300
        image3_x = get_position()  
    else:
        image3_y += dm
        
    return image3_x, image3_y


def image4_display(dm, image4_x, image4_y, screen):
    
    if image4_y > 350:
        image4_y = -600
        image4_x = get_position()  
    else:
        image4_y += dm
        
    return image4_x, image4_y
    
        
def get_position():
    return randint(0, screen_width - 75)
  

if __name__ == '__main__':
    display()
    