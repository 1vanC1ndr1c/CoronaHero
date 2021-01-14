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

        self.door_entrance_1 = Image.open(str(os.path.join(self._resources_path, 'Door-Entrance-1.png')))
        self.door_entrance_1 = transform_into_surface(self.door_entrance_1)

        self.door_exit = Image.open(str(os.path.join(self._resources_path, 'Door-Exit.png')))
        self.door_exit = transform_into_surface(self.door_exit)

        self.door_exit_1 = Image.open(str(os.path.join(self._resources_path, 'Door-Exit-1.png')))
        self.door_exit_1 = transform_into_surface(self.door_exit_1)

        self.width = self.door_entrance.get_width()
        self.height = self.door_entrance.get_height()
        self.set_dimensions(self.width, self.height)

        self.x_pos = 0
        self.y_pos = 0

    def set_dimensions(self, w, h):
        self.door_entrance = smoothscale(self.door_entrance, (w, h))
        self.door_entrance_1 = smoothscale(self.door_entrance_1, (w, h))
        self.door_exit = smoothscale(self.door_exit, (w, h))
        self.door_exit_1 = smoothscale(self.door_exit_1, (w, h))