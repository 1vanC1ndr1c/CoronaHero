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
platformImages = []
boxes = []
sinks = []
masks = []
disinfectants = []
gloves = []
doors = []
##dodaj set
inf_pers = []
viruses = []
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


def setPlatform(x, y, size, image):
    for i in range(size):
        platforms.append(Platform())
        platforms[len(platforms) - 1].set_dimensions(50, 50)
        platforms[len(platforms) - 1].set_position(x + i * 50, y)
        platforms[len(platforms) - 1].set_position(x + i * 50, y)
        platformImages.append(image)


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


def start_level_5(win):
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
               win = win
               )


def level_5(test,win):
    for i in range(103):
        # set floors
        if (i > 22 and i < 25) or i == 60:
            setPlatform(i * 50, 670, 1, 1)
        else:
            setPlatform(i * 50, 670, 1, 0)

    setPlatform(250, 520, 4, 0)
    setBox(280, 470)

    setPlatform(170, 300, 2, 0)
    setDisinfect(170, 250)

    setPlatform(650, 470, 3, 0)

    setPlatform(950, 370, 10, 0)
    setPlatform(1000, 420, 8, 1)
    setPlatform(1100, 470, 4, 1)
    setPlatform(1150, 520, 2, 1)
    setPlatform(1150, 570, 2, 1)
    setPlatform(1150, 620, 2, 1)

    setVirus(250,620)
    setVirus(265,620)
    setVirus(280,620)
    setVirus(295,620)
    setVirus(310,620)

    setBox(1140, 320)
    setSink(1250, 620)

    setPlatform(1600, 200, 1, 0)
    setDisinfect(1600, 150)

    for i in range(4):
        setPlatform(1800 + i * 70, 50 + 150 * i, 7, 0)
        if i != 0:
            setBox(1870 + i * 80, 150 * i)
            setBox(2030 + i * 80, 150 * i)
        for y in range(3):
            setBox(1870 + i * 250, 620)

    setPlatform(2500, 350, 4, 0)
    setBox(2550, 300)

    for i in range(9):
        setPlatform(3000, 620 - i * 50, 1, 1)

    setPlatform(2900, 170, 8, 0)
    setBox(3050, 120)

    setPlatform(3050, 350, 5, 0)
    setSink(3050, 300)

    for i in range(11):
        if i == 0:
            setPlatform(3500, 10, 1, 0)
            setPlatform(4100, 170, 1, 0)
        else:
            setPlatform(3500, 10 + i * 50, 1, 1)
            setPlatform(4100, 170 + i * 50, 1, 1)

    setPlatform(3550, 510, 9, 0)
    setPlatform(3550, 150, 9, 0)
    setPlatform(3700, 350, 8, 0)
    setPlatform(3450, 280, 1, 0)
    setSink(3550, 100)
    setBox(3950, 620)
    setBox(3800, 300)

    # border
    for i in range(12):
        setWall(0, 720 - 100 - 50 * i)
        setWall(1230 + 1280 * 2 + 640, 720 - 100 - 50 * i)

    setDoors(60, 570)
    setDoors(1140 + 1280 * 2 + 640, 570)

    # fill level surface
    level = pygame.Surface((1280 * 3 + 640, 720))  # 960, 640
    count = 0

    background = Background()
    background.set_dimensions(1280, 720)
    level.blit(background.image_cave, (0, 0))
    level.blit(background.image_cave, (1280, 0))
    level.blit(background.image_cave, (1280 * 2, 0))
    level.blit(background.image_cave, (1280 * 3, 0))

    for i in range(len(floors)):
        level.blit(floors[i].image_wall_darker, (floors[i].x_pos, floors[i].y_pos))

    for i in range(len(platforms)):
        if platformImages[i] == 1:
            level.blit(platforms[i].image_soil, (platforms[i].x_pos, platforms[i].y_pos))
        else:
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
            pygame.time.delay(6)

            win.fill((0, 0, 0))
            win.blit(level, (0 - (count * 5), 0))
            count += 1
            pygame.display.update()

        pygame.quit()


    # if not for testing return level surface
    else:
        return start_level_5(win)


if __name__ == '__main__':
    level_5(True)
