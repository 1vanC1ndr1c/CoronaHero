import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite
from pygame.transform import smoothscale

from corona_hero_app.image_handler import transform_into_surface


class Wall(Sprite):

    def __init__(self):
        Sprite.__init__(self)

        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")
        self.image_wall_brighter = Image.open(str(os.path.join(self._resources_path, 'Wall_Brighter.png')))
        self.image_wall_brighter = transform_into_surface(self.image_wall_brighter)
        self.image_wall_darker = Image.open(str(os.path.join(self._resources_path, 'Wall_Darker.png')))
        self.image_wall_darker = transform_into_surface(self.image_wall_darker)

        self.width = 300
        self.height = 300
        self.set_dimensions(self.width, self.height)

        self.x_pos = 0
        self.y_pos = 0

    def set_dimensions(self, w, h):
        self.image_wall_brighter = smoothscale(self.image_wall_brighter, (w, h))
        self.image_wall_darker = smoothscale(self.image_wall_darker, (w, h))
