import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite
from corona_hero_app.gif_splitter import split_animated_gif


class Enemy(Sprite):

    def __init__(self):
        Sprite.__init__(self)
        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")
        self._gif_L = Image.open(str(os.path.join(self._resources_path, 'virus-left.gif')))
        self._gif_R = Image.open(str(os.path.join(self._resources_path, 'virus-right.gif')))
        self._images_L = split_animated_gif(self._gif_L)
        self._images_R = split_animated_gif(self._gif_R)
        self.image_L = self._images_L[0]
        self.image_R = self._images_R[0]

        self.width = 50
        self.height = 100

        self.x_pos = 0
        self.y_pos = 0

        self._frame_counter = 0

    def animate(self):
        self.image = self._images_L[self._frame_counter]
        self._frame_counter = self._frame_counter + 1
        if self._frame_counter == 6:
            self._frame_counter = 0
