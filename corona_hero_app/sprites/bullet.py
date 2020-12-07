import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite
from pygame.transform import smoothscale

from corona_hero_app.image_handler import transform_into_surface


class Bullet(Sprite):

    def __init__(self, direction: str, start_pos_x: int, start_pos_y: int):
        Sprite.__init__(self)

        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")
        self.image_bullet = Image.open(str(os.path.join(self._resources_path, 'Bullet.png')))
        self.image_bullet = transform_into_surface(self.image_bullet)

        self.width = 30
        self.height = 30
        self.set_dimensions(self.width, self.height)

        self.x_pos = start_pos_x
        self.y_pos = start_pos_y

        self.direction = direction  # Or self.direction = "Right.

    def set_dimensions(self, w, h):
        self.image_bullet = smoothscale(self.image_bullet, (w, h))

    def bullet_travel(self):
        # TODO Limits based on a level size.
        if self.direction == "Left.":
            self.x_pos = self.x_pos - 10
        elif self.direction == "Right.":
            self.x_pos = self.x_pos + 10
