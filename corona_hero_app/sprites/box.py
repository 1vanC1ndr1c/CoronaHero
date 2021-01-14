import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite
from pygame.transform import smoothscale

from corona_hero_app.image_handler import transform_into_surface


class Box(Sprite):

    def __init__(self):
        Sprite.__init__(self)

        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")
        self.image_box = Image.open(str(os.path.join(self._resources_path, 'Box.png')))
        self.image_box = transform_into_surface(self.image_box)

        self.rect = self.image_box.get_rect()

        self.width = 30
        self.height = 30
        self.set_dimensions(self.width, self.height)

        self.rect.x = 150
        self.rect.y = 150

        self.x_pos = self.rect.x
        self.y_pos = self.rect.y

        self.rect.width = 30
        self.rect.height = 30

        self.is_dead = False

    def set_dimensions(self, w, h):
        self.rect.width = w
        self.rect.height = h
        self.width = w
        self.height = h
        self.image_box = smoothscale(self.image_box, (w, h))

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.x_pos = x
        self.y_pos = y

    def check_if_hit(self, bullet):
        bullet_range_x = range(bullet.x_pos, bullet.x_pos + bullet.width)
        bullet_range_y = range(bullet.y_pos, bullet.y_pos + bullet.height)

        self_range_x = range(self.rect.x, self.rect.x + self.width)
        self_range_y = range(self.rect.y, self.rect.y + self.height)

        if bool(set(bullet_range_x) & set(self_range_x)) is True:
            return bool(set(bullet_range_y) & set(self_range_y))

    def move(self, x_change, character):
        char_x = character.x_pos
        char_y = character.y_pos

        self_range_y = range(self.y_pos + self.height - 15, self.y_pos + self.height + 15)
        if (char_y + character.height) in self_range_y:
            if char_x < self.x_pos:
                self.x_pos = self.x_pos + x_change
            else:
                self.x_pos = self.x_pos - x_change
            self.rect.x = self.x_pos

    def get_rect(self):
        return self.rect
