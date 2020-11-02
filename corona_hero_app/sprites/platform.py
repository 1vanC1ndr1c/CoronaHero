import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite
from pygame.transform import smoothscale

from image_handler import transform_into_surface


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

        self.width = 50
        self.height = 100
        self.set_dimensions(self.width, self.height)

        self.x_pos = 0
        self.y_pos = 0

    def set_dimensions(self, w, h):
        self.image_grass = smoothscale(self.image_grass, (w, h))
        self.image_soil = smoothscale(self.image_soil, (w, h))
        self.image_concrete = smoothscale(self.image_concrete, (w, h))
