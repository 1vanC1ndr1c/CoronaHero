import sys
import pygame

sys.path.insert(1, '..')

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
    pygame.mixer.music.load("../resources/sounds/MainMusic.mp3")
    pygame.mixer.music.play()
    # start_test_level()  # Start the testing environment.

    level_done = False
    while level_done is False:
        level_done = level_1(False,win)
    level_done = False
    while level_done is False:
        level_done = level_2(False,win)
    level_done = False
    while level_done is False:
        level_done = level_3(False,win)
    level_done = False
    while level_done is False:
        level_done = level_4(False,win)
    level_done = False
    while level_done is False:
        level_done = level_5(False,win)
    
    pygame.quit()

if __name__ == '__main__':
    sys.exit(main())
