import pygame
import random
from sprites.main_character import MainCharacter
from sprites.enemy import Enemy
from sprites.platform import Platform
from sprites.box import Box
from sprites.bullet import Bullet
from sprites.disinfectant import Disinfectant
from sprites.gloves import Gloves
from sprites.infected_person import InfectedPerson
from sprites.mask import Mask
from sprites.sink import Sink
from sprites.wall import Wall

floors = []
platforms = []

def setFloor(x,y):
    floors.append( Wall())
    floors[len(floors) -1].set_dimensions(100,30) 
    floors[len(floors) -1].y_pos = y
    floors[len(floors) -1].x_pos = x

def setPlatform(x,y,size):
    for i in range(size):
        platforms.append( Platform())
        platforms[len(platforms)-1].set_dimensions(50, 50) 
        platforms[len(platforms)-1].x_pos = x+i*50
        platforms[len(platforms)-1].y_pos = y

def level_1(test):

    

    for i in range(40):
        #set floors
        setFloor(i*100,610 )
     
    for i in range(80):
        if i%9 == 0:
            #set platforms
            random.seed()
            size= random.randint(3,8) 
            height = random.randint(160,520)
            height = height-(height % 20)
            setPlatform(i*50, height, size)
        

    #fill level surface
    level = pygame.Surface((6000, 640))
    count = 0
    for i in range(40):
        level.blit(floors[i].image_wall_darker, (floors[i].x_pos,floors[i].y_pos ))

    for i in range(len(platforms)):
        level.blit(platforms[i].image_grass, (platforms[i].x_pos,platforms[i].y_pos ))
        count +=1

    #---for testing only
    if test:
         window_x_size = 960
         window_y_size = 640
         pygame.init()

         win = pygame.display.set_mode((window_x_size, window_y_size))

         pygame.display.set_caption("Testing environment.")
         count = 0
         while True:
             pygame.time.delay(40)
        
             win.fill((0, 0, 0))
             win.blit(level, (0-(count*5),0))
             count += 1
             pygame.display.update()

        
         pygame.quit()
    #if not for testing return level surface
    else : 
         return level

if __name__ == '__main__':
    level_1(True)
