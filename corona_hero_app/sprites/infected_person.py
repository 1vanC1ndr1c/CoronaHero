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
