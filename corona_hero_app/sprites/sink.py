import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite
from pygame.transform import smoothscale

from corona_hero_app.image_handler import transform_into_surface


class Sink(Sprite):

    def __init__(self):
        Sprite.__init__(self)

        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")
        self.image_sink = Image.open(str(os.path.join(self._resources_path, 'Sink.png')))
        self.image_sink = transform_into_surface(self.image_sink)

        self.rect = self.image_sink.get_rect()

        self.width = 30
        self.height = 30
        self.set_dimensions(self.width, self.height)

        self.rect.x = 0
        self.rect.y = 0

        self.x_pos = 0
        self.y_pos = 0

    def set_dimensions(self, w, h):
        self.image_sink = smoothscale(self.image_sink, (w, h))
        self.rect.width = 30
        self.rect.height = 30

    def get_rect(self):
        return self.rect
