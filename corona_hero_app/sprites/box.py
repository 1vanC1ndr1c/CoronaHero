import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite
from pygame.transform import smoothscale

from image_handler import transform_into_surface


class Box(Sprite):

    def __init__(self):
        Sprite.__init__(self)

        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")
        self.image_box = Image.open(str(os.path.join(self._resources_path, 'Box.png')))
        self.image_box = transform_into_surface(self.image_box)

        self.width = 30
        self.height = 30
        self.set_dimensions(self.width, self.height)

        self.x_pos = 0
        self.y_pos = 0

    def set_dimensions(self, w, h):
        self.image_box = smoothscale(self.image_box, (w, h))
