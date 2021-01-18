import sys
import pygame

sys.path.insert(1, '..')


import sys
sys.path.insert(0, "C:/Users/MISLAV/Desktop/korona projekt/projekt")

from corona_hero_app.levels.MainMenu import *
from corona_hero_app.levels.level_1 import level_1
from corona_hero_app.levels.level_2 import level_2
from corona_hero_app.levels.level_3 import level_3
from corona_hero_app.levels.level_4 import level_4
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

    lvl = -1
    carryOn = True
    retval = 0

    while carryOn:
        pos = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

        level_done = False
        lvl+=1
            
        if(lvl==0):
            bckgrnd = pygame.transform.scale(pygame.image.load(mmenu.background),(window_x_size,window_y_size))
            win.blit(bckgrnd,(0,0))
            
            retval = mmenu.make_menu(win,retval,pos)

            if(retval == 1):
                level_done = True
                pygame.mixer.music.load("../resources/sounds/MainMusic.mp3")
                pygame.mixer.music.play(loops=-1)
                retval = 0
                continue
            elif(retval==4):
                pygame.quit()
                exit(0)
            level_done = False
            pygame.display.update()
        
        elif(lvl==1):
            level_done = level_1(False,win)
        elif(lvl==2):
            level_done = level_2(False,win)
        elif(lvl==3):
            level_done = level_3(False,win)
        elif(lvl==4):
            level_done = level_4(False,win)
        elif(lvl==5):
            level_done = level_5(False,win)
        else:
            pygame.quit()
        if not level_done:
            lvl = -1

    
    pygame.quit()

if __name__ == '__main__':
    sys.exit(main())
