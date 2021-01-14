import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite
from pygame.transform import smoothscale

from corona_hero_app.image_handler import transform_into_surface


class Platform(Sprite):
    """
    This class has 3 images that can be chosen (grass, soil, concrete).
    Dimensions of the platform can be set with 'set_dimensions' method.
    """

    def __init__(self):
        Sprite.__init__(self)
        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")

        self.image_grass = Image.open(str(os.path.join(self._resources_path, 'Platform_Grass.png')))
        self.image_grass = transform_into_surface(self.image_grass)

        self.image_soil = Image.open(str(os.path.join(self._resources_path, 'Platform_Soil.png')))
        self.image_soil = transform_into_surface(self.image_soil)

        self.image_concrete = Image.open(str(os.path.join(self._resources_path, 'Platform_Concrete.png')))
        self.image_concrete = transform_into_surface(self.image_concrete)

        self.rect = self.image_grass.get_rect()

        self.width = 50
        self.height = 100
        self.set_dimensions(self.width, self.height)

        self.rect.x = 0
        self.rect.y = 0
        self.width = 50
        self.height = 100

        self.x_pos = 0
        self.y_pos = 0

        self.is_dead = False

    def set_dimensions(self, w, h):
        self.rect.width = w + 10
        self.rect.height = h + 10
        self.image_grass = smoothscale(self.image_grass, (w, h))
        self.image_soil = smoothscale(self.image_soil, (w, h))
        self.image_concrete = smoothscale(self.image_concrete, (w, h))

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.x_pos = x
        self.y_pos = y

    def check_if_hit(self, bullet):
        bullet_range_x = range(bullet.x_pos, bullet.x_pos + bullet.width)
        bullet_range_y = range(bullet.y_pos, bullet.y_pos + bullet.height)

        self_range_x = range(self.x_pos, self.x_pos + self.width)
        self_range_y = range(self.y_pos, self.y_pos + self.height)

        if bool(set(bullet_range_x) & set(self_range_x)) is True:
            return bool(set(bullet_range_y) & set(self_range_y))
