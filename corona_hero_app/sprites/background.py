import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite
from pygame.transform import smoothscale

from image_handler import transform_into_surface


class Background(Sprite):

    def __init__(self):
        Sprite.__init__(self)

        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")

        self.image_cave = Image.open(str(os.path.join(self._resources_path, 'Background-Cave.png')))
        self.image_cave = transform_into_surface(self.image_cave)

        self.width = 960
        self.height = 640
        self.set_dimensions(self.width, self.height)

        self.x_pos = 0
        self.y_pos = 0

    def set_dimensions(self, w, h):
        self.image_cave = smoothscale(self.image_cave, (w, h))
       