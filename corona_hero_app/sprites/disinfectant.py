import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite
from pygame.transform import smoothscale

from corona_hero_app.image_handler import transform_into_surface


class Disinfectant(Sprite):

    def __init__(self):
        Sprite.__init__(self)

        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")
        self.image_disinfectant = Image.open(str(os.path.join(self._resources_path, 'Disinfectant.png')))
        self.image_disinfectant = transform_into_surface(self.image_disinfectant)

        self.width = 30
        self.height = 30
        self.set_dimensions(self.width, self.height)

        self.x_pos = 0
        self.y_pos = 0

    def set_dimensions(self, w, h):
        self.image_disinfectant = smoothscale(self.image_disinfectant, (w, h))
