import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite
from pygame.transform import smoothscale

from image_handler import transform_into_surface


class Door(Sprite):

    def __init__(self):
        Sprite.__init__(self)

        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")

        self.image_entrance = Image.open(str(os.path.join(self._resources_path, 'Door-Entrance.png')))
        self.image_entrance = transform_into_surface(self.image_entrance)

        self.image_exit = Image.open(str(os.path.join(self._resources_path, 'Door-Exit.png')))
        self.image_exit = transform_into_surface(self.image_exit)

        self.width = 40
        self.height = 100
        self.set_dimensions(self.width, self.height)

        self.x_pos = 0
        self.y_pos = 0

    def set_dimensions(self, w, h):
        self.image_entrance = smoothscale(self.image_entrance, (w, h))
        self.image_exit = smoothscale(self.image_exit, (w, h))