import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite
from pygame.transform import smoothscale

from corona_hero_app.image_handler import transform_into_surface
from corona_hero_app.image_handler import split_animated_gif


class Mask(Sprite):

    def __init__(self):
        Sprite.__init__(self)

        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")

        self.image_mask_1 = Image.open(str(os.path.join(self._resources_path, 'Mask.gif')))
        self.image_mask_1 = split_animated_gif(self.image_mask_1)
        self.image_mask_1 = self.image_mask_1[0]

        self.image_mask_2 = Image.open(str(os.path.join(self._resources_path, 'Mask-v2.gif')))
        self.image_mask_2 = split_animated_gif(self.image_mask_2)
        self.image_mask_2 = self.image_mask_2[0]

        self.image_mask_3 = Image.open(str(os.path.join(self._resources_path, 'Mask-v3.gif')))
        self.image_mask_3 = split_animated_gif(self.image_mask_3)
        self.image_mask_3 = self.image_mask_3[0]

        self.width = 30
        self.height = 30
        self.set_dimensions(self.width, self.height)

        self.x_pos = 0
        self.y_pos = 0

    def set_dimensions(self, w, h):
        self.image_mask_1 = smoothscale(self.image_mask_1, (w, h))
        self.image_mask_2 = smoothscale(self.image_mask_1, (w, h))
        self.image_mask_3 = smoothscale(self.image_mask_1, (w, h))
