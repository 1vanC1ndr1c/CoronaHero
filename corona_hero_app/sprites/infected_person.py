import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite
from pygame.transform import smoothscale

from corona_hero_app.image_handler import transform_into_surface


class InfectedPerson(Sprite):

    def __init__(self):
        Sprite.__init__(self)

        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")
        self.image_infected_person = Image.open(str(os.path.join(self._resources_path, 'Infected_Person.png')))
        self.image_infected_person = transform_into_surface(self.image_infected_person)

        self.width = 100
        self.height = 150
        self.set_dimensions(self.width, self.height)

        self.x_pos = 0
        self.y_pos = 0

    def set_dimensions(self, w, h):
        self.image_infected_person = smoothscale(self.image_infected_person, (w, h))

    def is_hit(self, bullet):
        bullet_range_x = range(bullet.x_pos, bullet.x_pos + bullet.width)
        bullet_range_y = range(bullet.y_pos, bullet.y_pos + bullet.height)

        self_range_x = range(self.x_pos, self.x_pos + self.width)
        self_range_y = range(self.y_pos, self.y_pos + self.height)

        if bool(set(bullet_range_x) & set(self_range_x)) is True:
            return bool(set(bullet_range_y) & set(self_range_y))
