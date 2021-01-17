import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite
from pygame.transform import smoothscale

from corona_hero_app.image_handler import transform_into_surface


class Door(Sprite):

    def __init__(self):
        Sprite.__init__(self)

        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")

        self.door_entrance = Image.open(str(os.path.join(self._resources_path, 'Door-Entrance.png')))
        self.door_entrance = transform_into_surface(self.door_entrance)

        self.door_exit = Image.open(str(os.path.join(self._resources_path, 'Door-Exit.png')))
        self.door_exit = transform_into_surface(self.door_exit)

        self.width = self.door_entrance.get_width()
        self.height = self.door_entrance.get_height()
        self.set_dimensions(self.width, self.height)

        self.x_pos = 0
        self.y_pos = 0

    def set_dimensions(self, w, h):
        self.door_entrance = smoothscale(self.door_entrance, (w, h))
        self.door_exit = smoothscale(self.door_exit, (w, h))
    def check_if_hit(self, el):
        el_range_x = range(el.x_pos, el.x_pos + el.width)
        el_range_y = range(el.y_pos, el.y_pos + el.height)

        self_range_x = range(self.x_pos, self.x_pos + self.width)
        self_range_y = range(self.y_pos, self.y_pos + self.height)

        if bool(set(el_range_x) & set(self_range_x)) is True:
            return bool(set(el_range_y) & set(self_range_y))
