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
from sprites.door import Door
from sprites.background import Background


floors = []
platforms = []
boxes = []
sinks = []
masks = []
disinfectants = []
gloves = []
doors = []


def setWall(x,y):
    floors.append( Wall())
    floors[len(floors) -1].set_dimensions(50,50) 
    floors[len(floors) -1].y_pos = y
    floors[len(floors) -1].x_pos = x

def setPlatform(x,y,size):
    for i in range(size):
        platforms.append( Platform())
        platforms[len(platforms)-1].set_dimensions(50, 50) 
        platforms[len(platforms)-1].x_pos = x+i*50
        platforms[len(platforms)-1].y_pos = y

def setBox(x,y):
    boxes.append( Box())
    boxes[len(boxes) -1].set_dimensions(50,50) 
    boxes[len(boxes) -1].y_pos = y
    boxes[len(boxes) -1].x_pos = x

def setSink(x,y):
    sinks.append( Sink())
    sinks[len(sinks) -1].set_dimensions(50,50) 
    sinks[len(sinks) -1].y_pos = y
    sinks[len(sinks) -1].x_pos = x

def setMask(x,y):
    masks.append( Mask())
    masks[len(masks) -1].set_dimensions(30,30) 
    masks[len(masks) -1].y_pos = y
    masks[len(masks) -1].x_pos = x

def setGloves(x,y):
    gloves.append( Gloves())
    gloves[len(gloves) -1].set_dimensions(30,30) 
    gloves[len(gloves) -1].y_pos = y
    gloves[len(gloves) -1].x_pos = x


def setDisinfect(x,y):
    disinfectants.append( Disinfectant())
    disinfectants[len(disinfectants) -1].set_dimensions(25,45) 
    disinfectants[len(disinfectants) -1].y_pos = y
    disinfectants[len(disinfectants) -1].x_pos = x

def setDoors(x,y):
    doors.append( Door())
    doors[len(doors) -1].set_dimensions(70,100) 
    doors[len(doors) -1].y_pos = y
    doors[len(doors) -1].x_pos = x




def level_test1(test):

    for i in range(20):
       #set floors
       setPlatform(i*50,590,1)

    #border
    for i in range(5):
        setWall(0, 640-100-50*i)
        setWall(910, 640-100-50*i)

    setPlatform(170, 450, 5)
    setPlatform(500, 250, 3)
    setPlatform(300, 100, 2)
    setPlatform(500,540,2)
    setSink(600, 540)
    #setMask(310, 70)
    setDisinfect(180, 405)
    setDoors(60,490)
    setDoors(820,490)

    #fill level surface
    level = pygame.Surface((960, 640))
    count = 0

    background = Background()
    background.set_dimensions(960,640)
    level.blit(background.image_cave, (0,0))

    for i in range (len(floors)):
        level.blit(floors[i].image_wall_darker, (floors[i].x_pos,floors[i].y_pos ))

    for i in range (len(platforms)):
        if i == 11 or i == 10:
            level.blit(platforms[i].image_soil, (platforms[i].x_pos,platforms[i].y_pos ))
            continue
        level.blit(platforms[i].image_grass, (platforms[i].x_pos,platforms[i].y_pos ))


    for i in range (len(sinks)):
        level.blit(sinks[i].image_sink, (sinks[i].x_pos,sinks[i].y_pos ))

    for i in range (len(disinfectants)):
        level.blit(disinfectants[i].image_disinfectant, (disinfectants[i].x_pos,disinfectants[i].y_pos ))

    level.blit(doors[0].image_entrance, (doors[0].x_pos,doors[0].y_pos ))
    level.blit(doors[1].image_exit, (doors[1].x_pos,doors[1].y_pos ))



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
             #count += 1
             pygame.display.update()

        
         pygame.quit()


    #if not for testing return level surface
    else : 
         return level



if __name__ == '__main__':
    level_test1(True)