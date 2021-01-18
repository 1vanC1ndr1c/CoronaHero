import pygame
from engine.engine import start_game
from sprites.background import Background
from sprites.box import Box
from sprites.disinfectant import Disinfectant
from sprites.door import Door
from sprites.gloves import Gloves
from sprites.main_character import MainCharacter
from sprites.mask import Mask
from sprites.platform import Platform
from sprites.sink import Sink
from sprites.virus import Virus
from sprites.wall import Wall

floors = []
platforms = []
boxes = []
sinks = []
masks = []
disinfectants = []
gloves = []
doors = []
inf_pers = []
viruses = []
##dodaj set

backgrounds = []


def setVirus(x,y):
    viruses.append(Virus())
    viruses[len(viruses)-1].set_dimensions(50,50)
    viruses[len(viruses)-1].y_pos = y
    viruses[len(viruses)-1].x_pos = x
    viruses[len(viruses)-1].set_position(x,y)


def setBackground(x, y):
    backgrounds.append(Background())
    backgrounds[len(backgrounds) - 1].set_dimensions(1280, 720)
    backgrounds[len(backgrounds) - 1].y_pos = y
    backgrounds[len(backgrounds) - 1].x_pos = x


def setWall(x, y):
    floors.append(Wall())
    floors[len(floors) - 1].set_dimensions(50, 50)
    floors[len(floors) - 1].y_pos = y
    floors[len(floors) - 1].x_pos = x
    floors[len(floors) - 1].set_position(x, y)


def setPlatform(x, y, size):
    for i in range(size):
        platforms.append(Platform())
        platforms[len(platforms) - 1].set_dimensions(50, 50)
        platforms[len(platforms) - 1].x_pos = x + i * 50
        platforms[len(platforms) - 1].y_pos = y
        platforms[len(platforms) - 1].set_position(x + i * 50, y)


def setBox(x, y):
    boxes.append(Box())
    boxes[len(boxes) - 1].set_dimensions(50, 50)
    boxes[len(boxes) - 1].set_position(x, y)


def setSink(x, y):
    sinks.append(Sink())
    sinks[len(sinks) - 1].set_dimensions(50, 50)
    sinks[len(sinks) - 1].y_pos = y
    sinks[len(sinks) - 1].x_pos = x


def setMask(x, y):
    masks.append(Mask())
    masks[len(masks) - 1].set_dimensions(30, 30)
    masks[len(masks) - 1].y_pos = y
    masks[len(masks) - 1].x_pos = x


def setGloves(x, y):
    gloves.append(Gloves())
    gloves[len(gloves) - 1].set_dimensions(30, 30)
    gloves[len(gloves) - 1].y_pos = y
    gloves[len(gloves) - 1].x_pos = x


def setDisinfect(x, y):
    disinfectants.append(Disinfectant())
    disinfectants[len(disinfectants) - 1].set_dimensions(25, 45)
    disinfectants[len(disinfectants) - 1].y_pos = y
    disinfectants[len(disinfectants) - 1].x_pos = x


def setDoors(x, y):
    doors.append(Door())
    doors[len(doors) - 1].set_dimensions(70, 100)
    doors[len(doors) - 1].y_pos = y
    doors[len(doors) - 1].x_pos = x


def start_level_3(win):
    character = MainCharacter()  # Check the main character animation
    character.set_position(130, 570)

    virus = Virus()  # ... or check the virus animation.

    return start_game(character=character,
               platforms=platforms,
               boxes=boxes,
               dis=disinfectants,
               gloves=gloves,
               inf_per=inf_pers,
               masks=masks,
               sinks=sinks,
               walls=floors,
               viruses=viruses,
               rects=platforms + boxes + floors,
               doors=doors,
               backgrounds=backgrounds,
               win=win
               )


def level_3(test,win):
    for i in range(26):
        # set floors
        setPlatform(i * 50, 670, 1)

    # border
    for i in range(12):
        setWall(0, 720 - 100 - 50 * i)
        setWall(1230, 720 - 100 - 50 * i)

    # set middle wall
    for i in range(10):
        setPlatform(600, 620 - 50 * i, 1)
    setPlatform(350, 120, 6)

    # set door wall
    for i in range(6):
        setPlatform(1050, 620 - 50 * i, 1)

    setPlatform(70, 470, 3)
    setPlatform(550, 530, 1)
    setPlatform(320, 370, 4)
    setPlatform(120, 220, 2)
    setPlatform(720, 550, 5)
    setPlatform(500, 70, 1)

    setVirus(250,620)
    setVirus(410,70)
    setVirus(670,620)
    setVirus(950,620)
    setVirus(820,500)

    setGloves(350, 620)
    setGloves(1000,620)

    setSink(550, 70)
    setBox(450, 620)
    setBox(410, 320)
    setBox(750, 500)

    setDoors(60, 570)
    setDoors(1140, 570)

    # fill level surface
    level = pygame.Surface((1280, 720))  # 960, 640
    count = 0

    background = Background()
    background.set_dimensions(1280, 720)
    level.blit(background.image_cave, (0, 0))
    setBackground(0, 0)

    for i in range(len(floors)):
        level.blit(floors[i].image_wall_darker, (floors[i].x_pos, floors[i].y_pos))

    for i in range(len(platforms)):
        if (i > 25 and i < 36) or i == 39 or i == 12 or (i > 41 and i < 47) or i == 21:
            level.blit(platforms[i].image_soil, (platforms[i].x_pos, platforms[i].y_pos))
            continue
        level.blit(platforms[i].image_grass, (platforms[i].x_pos, platforms[i].y_pos))

    for i in range(len(sinks)):
        level.blit(sinks[i].image_sink, (sinks[i].x_pos, sinks[i].y_pos))

    for i in range(len(disinfectants)):
        level.blit(disinfectants[i].image_disinfectant, (disinfectants[i].x_pos, disinfectants[i].y_pos))

    for i in range(len(boxes)):
        level.blit(boxes[i].image_box, (boxes[i].x_pos, boxes[i].y_pos))

    level.blit(doors[0].door_entrance, (doors[0].x_pos, doors[0].y_pos))
    level.blit(doors[1].door_exit, (doors[1].x_pos, doors[1].y_pos))

    # ---for testing only
    if test:
        window_x_size = 1280
        window_y_size = 720
        pygame.init()

        win = pygame.display.set_mode((window_x_size, window_y_size))

        pygame.display.set_caption("Testing environment.")
        count = 0
        while True:
            pygame.time.delay(40)

            win.fill((0, 0, 0))
            win.blit(level, (0 - (count * 5), 0))
            # count += 1
            pygame.display.update()

        pygame.quit()


    # if not for testing return level surface
    else:
        return start_level_3(win)


if __name__ == '__main__':
    level_3(True)
