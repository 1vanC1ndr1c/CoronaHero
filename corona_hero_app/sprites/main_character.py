import os
from pathlib import Path
from time import sleep

import pygame
from PIL import Image
from pygame.sprite import Sprite
from corona_hero_app.gif_splitter import split_animated_gif


class MainCharacter(Sprite):

    def __init__(self):
        Sprite.__init__(self)
        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")
        self._gif = Image.open(str(os.path.join(self._resources_path, 'Hero-GoodSize-still.gif')))
        self._images = split_animated_gif(self._gif)
        self.image = self._images[0]

        self.width = 50
        self.height = 100

        self.x_pos = 0
        self.y_pos = 0

        self._frame_counter = 0

    def animate(self):
        self.image = self._images[self._frame_counter]
        self._frame_counter = self._frame_counter + 1
        if self._frame_counter == 6:
            self._frame_counter = 0
