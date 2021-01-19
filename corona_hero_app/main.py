import sys
import pygame
import random

sys.path.insert(1, '..')


from corona_hero_app.sprites.energy_time import EnergyTime
from corona_hero_app.levels.MainMenu import *
from corona_hero_app.levels.level_1 import level_1
from corona_hero_app.levels.level_2 import level_2
from corona_hero_app.levels.level_3 import level_3 as level_4
from corona_hero_app.levels.level_4 import level_4 as level_3
from corona_hero_app.levels.level_5 import level_5    

def main():
    window_x_size = 1280
    window_y_size = 720
    pygame.init()
    win = pygame.display.set_mode((window_x_size, window_y_size))
    pygame.display.set_caption("Testing environment.")
    # start_test_level()  # Start the testing environment.
    mmenu = MainMenu()
    mmenu.add_button(window_x_size/2-125,200,"new game")
    mmenu.add_button(window_x_size/2-125,300,"help")
    mmenu.add_button(window_x_size/2-125,400,"about")
    mmenu.add_button(window_x_size/2-125,500,"exit")
    mmenu.add_button(window_x_size/2-125,610,"back")
    energy_time1 = EnergyTime(0, 0)
    energy_time2 = EnergyTime(0, 70)
    first_lesson = False
    lesson = 0
    lessonName = ""
    outro = 0

    lvl = -2
    carryOn = True
    retval = 0
    character = None
    intro = 110

    while carryOn:
        pos = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

        if(lesson>0):
            imtoblt = pygame.transform.scale(pygame.image.load("../resources/sprites/"+lessonName+".png"),(window_x_size,window_y_size))
            lesson-=1
            win.blit(imtoblt,(0,0))
            pygame.display.update()
            continue
        
        level_done = False
        lvl+=1

        if(lvl == -1):
            imtoblt = None
            if(intro>=100):
                imtoblt = pygame.transform.scale(pygame.image.load("../resources/sprites/TeamLogo.png"),(window_x_size,window_y_size))
            elif(intro>50 and intro<100):
                imtoblt = pygame.transform.scale(pygame.image.load("../resources/sprites/Presents.png"),(window_x_size,window_y_size))
            else:
                imtoblt = pygame.transform.scale(pygame.image.load("../resources/sprites/Title page artwork-Main.png"),(window_x_size,window_y_size))
            win.blit(imtoblt,(0,0))

            intro-=1
            if(intro==0):
                level_done = True
            
            pygame.display.update()
            pygame.time.delay(20)
            
        elif(lvl==0):
            bckgrnd = pygame.transform.scale(pygame.image.load(mmenu.background),(window_x_size,window_y_size))
            win.blit(bckgrnd,(0,0))
            
            retval = mmenu.make_menu(win,retval,pos)

            if(retval == 1):
                level_done = True
                pygame.mixer.music.load("../resources/sounds/MainMusic.mp3")
                pygame.mixer.music.play(loops=-1)
                retval = 0
                character = MainCharacter()
                continue
            elif(retval==4):
                pygame.quit()
                exit(0)
            level_done = False
            pygame.display.update()
        
        elif(lvl==1):
            first_lesson = True
            level_done = level_1(False,win,character,energy_time1,energy_time2)
        elif(lvl==2):
            level_done = level_2(False,win,character,energy_time1,energy_time2)
        elif(lvl==3):
            level_done = level_3(False,win,character,energy_time1,energy_time2)
        elif(lvl==4):
            level_done = level_4(False,win,character,energy_time1,energy_time2)
        elif(lvl==5):
            level_done = level_5(False,win,character,energy_time1,energy_time2)
            outro = 100
            first_lesson = False
        elif(lvl==6):
            outro-=1
            imtoblt = pygame.transform.scale(pygame.image.load("../resources/sprites/ThankYouForPlaying.png"),(window_x_size,window_y_size))
            win.blit(imtoblt,(0,0))
            pygame.display.update()
            
            if(outro==0):
                level_done = False
            else:
                continue
        else:
            pygame.quit()

        if not level_done:
            if(lvl>=0):
                lvl = -1
            else:
                lvl = -2
        else:
            if(first_lesson):
                lesson = 100
                lessonName = "DYN"+str(random.randint(1,8))
    
    pygame.quit()

if __name__ == '__main__':
    sys.exit(main())
