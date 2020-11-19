import pygame
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

def level_1(test):

    
    floors = []
    platforms = []
    for i in range(60):
        #set floors
        floors.append( Wall())
        floors[i].set_dimensions(100,30) 
        floors[i].y_pos = 610
        floors[i].x_pos = i*100
        #set platforms             
        if i % 3 == 0 or i % 7 == 0 or i%17 ==0:
            platforms.append( Platform())
            platforms[len(platforms)-1].set_dimensions(i%13*10+50, 30) 
            platforms[len(platforms)-1].x_pos = i*100
            platforms[len(platforms)-1].y_pos = 500 - (i%7)*50

    #fill level surface
    level = pygame.Surface((6000, 640))
    count = 0
    for i in range(60):
        level.blit(floors[i].image_wall_darker, (floors[i].x_pos,floors[i].y_pos ))
        if i % 3 == 0 or i % 7 == 0 or i%17 ==0:
            level.blit(platforms[count].image_grass, (platforms[count].x_pos,platforms[count].y_pos ))
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
         return level;

if __name__ == '__main__':
    level_1(True)
